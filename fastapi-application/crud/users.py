from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from sqlalchemy import select

async def get_all_users(session: AsyncSession) -> Sequence[User]:
    query = (
        select(User)
        .order_by(User.id)
    )
    result =  await session.scalars(query)
    return result.all()