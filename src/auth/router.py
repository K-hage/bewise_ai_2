from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas import UserCreateRequest, UserCreateResponse
from src.auth.service import create_user
from src.database import get_async_session

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.post('/')
async def user_create(
        new_request: UserCreateRequest,
        session: AsyncSession = Depends(get_async_session)
) -> UserCreateResponse:
    """
    Создает пользователя по полученному имени
    """

    user = await create_user(session, new_request)
    return UserCreateResponse.from_orm(user)
