from sqlalchemy import Column, String, DateTime, Integer, Float
from database_connection import Base, engine
from datetime import datetime


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    postal_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    created_time = Column(DateTime, default=datetime.utcnow)
    updated_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


Base.metadata.create_all(bind=engine)
