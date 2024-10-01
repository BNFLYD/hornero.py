from sqlalchemy import Column, BigInteger, Boolean, ForeignKey
from models.tables import Base

class MessageRequest(Base):
    __tablename__ = 'message_requests'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    sender_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    receiver_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    is_approved = Column(Boolean, default=False)