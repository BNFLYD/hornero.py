from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.tables import Base

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    post_id = Column(BigInteger, ForeignKey('posts.id'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    # Relaciones
    user = relationship("User", backref="comments")
    post = relationship("Post", backref="comments")
    
    # Relaciones polimórficas
    likes = relationship("Like", primaryjoin="and_(Comment.id==Like.content_id, Like.content_type=='comment')", backref="comment")
    reposts = relationship("Repost", primaryjoin="and_(Comment.id==Repost.content_id, Repost.content_type=='comment')", backref="comment")
    media = relationship("Media", back_populates="comment", cascade="all, delete-orphan")