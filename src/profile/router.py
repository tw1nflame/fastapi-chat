from fastapi import APIRouter


router = APIRouter(
    prefix="profile",
    tags=["profile"]
)


@router.get("/{id}")
async def get_profile_info(id: int):
    pass
