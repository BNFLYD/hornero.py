from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.sql import func
from models.tables import Base

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    sender_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=True)
    media_url = Column(Text, nullable=True)
    media_type = Column(Text, nullable=True)
    sent_at = Column(TIMESTAMP, server_default=func.now())
    is_read = Column(Boolean, default=False)