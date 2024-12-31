from datetime import datetime
from pydantic import BaseModel, Field
from auth.schemas import UserRead


class Profile_info(UserRead):
    # id: int
    # email: str
    # first_name: str
    # last_name: str
    user_id: int
    bio: str = Field(max_length=1000)
    status: str = Field(max_length=50)
    birth_date: datetime
