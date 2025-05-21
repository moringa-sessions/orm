from sqlalchemy import Column, Integer, DateTime, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50),unique=True, nullable=False )
    email= Column(String(50), nullable=False, unique=True )
    joined_on = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")
     

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(50),unique=True, nullable=False )
    description= Column(Text, nullable=False )
    due_date = Column(DateTime, nullable=True)
    status = Column(String(30), default="To Do", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id= Column(Integer, ForeignKey("categories.id"), nullable=False)

    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True, nullable=False )
   
    tasks = relationship("Task", back_populates="category")
