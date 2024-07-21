from fastapi import APIRouter, Depends

from core.config import settings
from core.schemas import UserRead
from core.models import db_helper
from crud.users import *

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"]
)

@router.get("/", response_model=list[UserRead])
async def get_users(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    users = await get_all_users(session)
    return users

@router.post("/create/", response_model=UserRead)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    user = await create_1_user(session, user_create)
    return user
