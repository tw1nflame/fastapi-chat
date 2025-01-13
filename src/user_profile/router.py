from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth.models import User
from database import get_async_session
from user_profile.schemas import Profile_info
from template import templates

router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)


@router.get("/{id}")
async def get_profile_info(request: Request, id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User).where(User.id == id))
    person = Profile_info.from_orm(result.scalars().first())
    return templates.TemplateResponse("profile.html", {"request": request, "person": person})
  

@router.post("/edit_profile")
async def edit_profile():
    pass
