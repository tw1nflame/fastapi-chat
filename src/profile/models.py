from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column, Mapped

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, MetaData, String, Table, func
from database import Base
from auth.models import User

metadata = MetaData()


class Profile_info(Base):
    __tablename__ = "profile_info"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey=User.id)
    bio: Mapped[str] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(String(1000))
    birth_date: Mapped[datetime] = mapped_column(TIMESTAMP)
