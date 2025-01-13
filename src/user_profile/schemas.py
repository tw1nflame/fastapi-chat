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