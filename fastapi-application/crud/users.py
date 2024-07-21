from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.models import User
from core.schemas import UserCreate

async def get_all_users(session: AsyncSession) -> Sequence[User]:
    query = (
        select(User)
        .order_by(User.id)
    )
    result =  await session.scalars(query)
    return result.all()

async def create_1_user(
    session: AsyncSession,
    user_create: UserCreate
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    return user
    