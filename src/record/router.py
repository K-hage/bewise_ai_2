from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, Query, File
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import FileResponse

from src.auth.auth_check import check_user
from src.record.schemas import AudioResponse
from src.record.service import save_audio_db, find_audio
from src.record.utils import url_for_download, check_extensions
from src.database import get_async_session

router = APIRouter(
    prefix='/record',
    tags=['record']
)


@router.post('/')
async def create_mp3(
        request: Request,
        user_id: UUID,
        access_token: str,

        audio_wav: Annotated[UploadFile, File(description="Приложите файл формата wav")],
        session: AsyncSession = Depends(get_async_session)

) -> AudioResponse:
    """
    Изменяет полученный wav файл в mp3
    """

    check_extensions(audio_wav)
    await check_user(session, user_id, access_token)
    audio = await save_audio_db(session, audio_wav, user_id)
    download_url = url_for_download(request, user_id, audio.id)
    return AudioResponse(download_url=download_url)


@router.get('')
async def download_mp3(
        id_: UUID = Query(alias='id', description='UUID трека'),
        user: UUID = Query(description='UUID пользователя'),
        session: AsyncSession = Depends(get_async_session)
) -> FileResponse:
    """
    Позволяет скачать Mp3-файл по указанным идентификаторам файла и пользователя
    """

    audio = await find_audio(session, id_, user)
    return FileResponse(path=audio.path, media_type='audio/mpeg')
