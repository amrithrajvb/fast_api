from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# from .database import Base
from connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    Phone = Column(Integer, index=True)
    hashed_password = Column(String)
    # profile_picture=Column(,index=True)
    is_active = Column(Boolean, default=True)



