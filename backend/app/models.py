from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))
    description = Column(String(255), nullable=True)
    links = relationship("Link", back_populates="owner")

class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    url = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="links")
