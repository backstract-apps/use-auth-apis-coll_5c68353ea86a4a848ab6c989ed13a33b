from sqlalchemy import Column, Integer, String, Boolean, DateTime, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persons(Base):
    __tablename__ = 'persons'
    rollnumber = Column(INTEGER, primary_key=True)
    fullname = Column(VARCHAR(100), primary_key=False)
    age = Column(INTEGER, primary_key=False)
    profession = Column(VARCHAR(50), primary_key=False)

