from uuid import UUID

from fastapi import HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.record.models import Audio
from src.record.utils import converter_audio, check_file


async def save_audio_db(session: AsyncSession, audio: UploadFile, user_id: UUID) -> Audio:
    """
    Преобразует аудио-файл и сохраняет данные о нем в бд
    :param session: экземпляр AsyncSession
    :param audio: файл для преобразования и сохранения в бд
    :param user_id: идентификатор пользователя
    :return: экземпляр Audio
    """

    async with session.begin():
        audio_path = await converter_audio(audio)
        try:
            db_audio = Audio(
                user_id=user_id,
                path=audio_path
            )
            session.add(db_audio)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise HTTPException(
                status_code=400, detail='Ошибка при создании записи'
            )
    if db_audio:
        return db_audio

    raise HTTPException(
        status_code=400, detail='Ошибка при создании пользователя'
    )


async def find_audio(session: AsyncSession, audio_id: UUID, user_id: UUID) -> Audio:
    """
    Ищет данные аудио-файла, проверяет его наличие в хранилище
    :param session: экземпляр AsyncSession
    :param audio_id: идентификатор файла
    :param user_id: идентификатор пользователя
    :return: экземпляр Audio
    """

    query = select(Audio).filter(Audio.id == audio_id, Audio.user_id == user_id)
    question = await session.execute(query)
    audio: Audio = question.scalar_one_or_none()
    check_file(audio.path)
    if audio is None:
        raise HTTPException(status_code=404, detail='Файл не найден')
    return audio
