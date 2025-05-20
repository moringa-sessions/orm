from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50),unique=True, nullable=False )
    email= Column(String(50), nullable=False, unique=True )
    joined_on = Column(DateTime, default=datetime.utcnow)



