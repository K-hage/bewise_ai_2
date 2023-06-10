from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User


async def check_user(session: AsyncSession, user_id: UUID, access_token: str) -> None:
    """
    Проверяет наличие данных пользователя
    :param session: экземпляр AsyncSession
    :param user_id: идентификатор пользователя
    :param access_token: токен пользователя
    """

    query = select(User).filter(User.id == user_id, User.access_token == access_token)
    question = await session.execute(query)
    user = question.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=403, detail='Доступ отсутствует')
    await session.commit()
