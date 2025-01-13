from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth.models import User
from database import get_async_session
from user_profile.schemas import Profile_info, UserEdit
from template import templates
from chat.router import current_user
router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)



@router.get("/{id}")
async def get_profile_info(request: Request, id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User).where(User.id == id))
    person = Profile_info.from_orm(result.scalars().first())
    return templates.TemplateResponse("profile.html", {"request": request, "person": person})
  

@router.put("/edit_profile")
async def edit_profile(request: Request, user_edit: UserEdit = Depends(), user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    if not user:
        raise HTTPException(status_code=401, detail="User not authenticated")
    
    update_data = user_edit.model_dump(exclude_unset=True) 
    
    for key, value in update_data.items():
        if value is not None:
            setattr(user, key, value)
        
    await session.commit()
    
    return {"message": "User updated successfully", "user": user}
    
