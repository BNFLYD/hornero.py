from sqlalchemy import Column, BigInteger, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from models.tables import Base

class ListMember(Base):
    __tablename__ = 'list_members'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    list_id = Column(BigInteger, ForeignKey('lists.id'), nullable=True)
    member_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    added_at = Column(TIMESTAMP, server_default=func.now())