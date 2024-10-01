from sqlalchemy import Column, BigInteger, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Media(Base):
    __tablename__ = 'media'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    file_path = Column(Text, nullable=False)
    post_id = Column(BigInteger, ForeignKey('posts.id', ondelete='CASCADE'), nullable=True)
    comment_id = Column(BigInteger, ForeignKey('comments.id', ondelete='CASCADE'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    post = relationship("Post", back_populates="media")
    comment = relationship("Comment", back_populates="media")