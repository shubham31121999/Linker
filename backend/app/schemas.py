from pydantic import BaseModel, EmailStr
from typing import List, Optional

class LinkBase(BaseModel):
    title: str
    url: str

class LinkCreate(LinkBase):
    pass

class LinkResponse(LinkBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserDashboard(BaseModel):
    description: Optional[str] = None
    links: List[LinkCreate]

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    description: Optional[str]
    links: List[LinkResponse] = []
    class Config:
        orm_mode = True
