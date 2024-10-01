from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.tables import Base
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    content = Column(Text)
    parent_post_id = Column(BigInteger, ForeignKey('posts.id'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    # Relaciónes con otras tablas
    parent_post = relationship("Post", remote_side=[id], backref="child_posts")
    media = relationship("Media", back_populates="post", cascade="all, delete-orphan")