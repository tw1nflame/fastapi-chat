from datetime import datetime
from pydantic import BaseModel, Field
from auth.schemas import UserRead
from typing import Optional


class Profile_info(UserRead):
    bio: Optional[str] = Field(max_length=1000)
    status: Optional[str] = Field(max_length=50)
    birth_date: Optional[datetime]
    class Config:
        from_attributes = True

class UserEdit(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    bio: Optional[str] = Field(max_length=1000, default=None)
    status: Optional[str] = Field(max_length=50, default=None)
    birth_date: Optional[datetime] = None
