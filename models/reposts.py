from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.tables import Base
class Repost(Base):
    __tablename__ = 'reposts'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    content_type = Column(Text, nullable=False)
    content_id = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    __table_args__ = (
        UniqueConstraint('user_id', 'content_type', 'content_id', name='unique_repost_per_user'),
    )
    
    # Relaciones polimórficas
    post = relationship("Post", primaryjoin="and_(Repost.content_id==Post.id, Repost.content_type=='post')", backref="reposts")
    comment = relationship("Comment", primaryjoin="and_(Repost.content_id==Comment.id, Repost.content_type=='comment')", backref="reposts")