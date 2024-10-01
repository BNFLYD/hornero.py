from sqlalchemy import Column, BigInteger, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from models.tables import Base

class Block(Base):
    __tablename__ = 'blocks'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    blocker_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    blocked_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())