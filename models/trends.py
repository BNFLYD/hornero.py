from sqlalchemy import Column, BigInteger, Text, TIMESTAMP
from sqlalchemy.sql import func
from models.tables import Base

class Trend(Base):
    __tablename__ = 'trends'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    hashtag = Column(Text, nullable=False)
    post_count = Column(BigInteger, default=0)
    last_updated = Column(TIMESTAMP, server_default=func.now())