from fastapi.staticfiles import StaticFiles
from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserCreate, UserRead
from typing import List
from fastapi import Depends, FastAPI
from auth_forms.router import router as login_router
from chat.router import router as chat_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(login_router)
app.include_router(chat_router)
