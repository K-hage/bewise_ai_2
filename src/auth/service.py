from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.schemas import UserCreateRequest, UserCreateResponse


async def create_user(session: AsyncSession, user: UserCreateRequest) -> User:
    async with session.begin():
        try:
            db_user = User(name=user.name)
            session.add(db_user)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=400, detail='Ошибка при создании пользователя'
            )
    if db_user:
        return db_user

    raise HTTPException(
        status_code=400, detail='Ошибка при создании пользователя'
    )
