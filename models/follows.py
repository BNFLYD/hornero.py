from sqlalchemy import Column, BigInteger, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models.tables import Base

class Follow(Base):
    __tablename__ = 'follows'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    follower_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    followed_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    is_approved = Column(Boolean, default=False)

    follower = relationship("User", foreign_keys=[follower_id])
    followed = relationship("User", foreign_keys=[followed_id])