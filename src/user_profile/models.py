from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column, Mapped

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, MetaData, String, Table, func
from database import Base
from auth.models import User

