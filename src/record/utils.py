import os
from uuid import uuid4

from fastapi import UploadFile, HTTPException
from pydub import AudioSegment
from starlette.requests import Request

from src.config import STORAGE_PATH, ALLOWED_EXTENSION


async def converter_audio(audio: UploadFile, ext_out: str = 'mp3', storage: str = STORAGE_PATH) -> str:
    """
    Асинхронная функция преобразования аудиофайлов
    :param audio: преобразуемый файл
    :param ext_out: формат выходного файла, по умолчанию mp3
    :param storage: место хранения файлов, по умолчанию src.config.STORAGE_PATH
    :return: путь к созданному файлу
    """

    ext = audio.filename.split('.')[-1]
    name = str(uuid4())
    input_path = storage + name + '.' + ext
    output_path = storage + name + '.' + ext_out
    with open(input_path, 'wb') as f:
        audio = await audio.read()
        f.write(audio)
    try:
        sound = AudioSegment.from_file(input_path, ext)
        sound.export(output_path, format=ext_out)
    except Exception as e:
        os.remove(input_path)
        raise HTTPException(
            status_code=500, detail='Ошибка преобразования'
        )

    check_file(output_path)
    return output_path


def url_for_download(request: Request, user_id, track_id) -> str:
    """
    Генерирует ссылку на скачивание файла
    :param request: экземпляр класса starlette.requests.Requests
    :param user_id: идентификатор пользователя
    :param track_id: идентификатор файла
    :return: url для загрузки файла
    """

    path = request.url_for('download_mp3')
    return f'{path}?id={track_id}&user={user_id}'


def check_file(path: str) -> None:
    """
    Проверяет наличие файла
    :param path: путь файла
    """

    if not os.path.isfile(path):
        raise HTTPException(
            status_code=404, detail='Не удалось создать или найти файл'
        )


def check_extensions(file: UploadFile, allowed_ext: list[str] = ALLOWED_EXTENSION):
    """
    Проверка поддерживаемых форматов
    :param file: проверяемый файл
    :param allowed_ext: список поддерживаемых расширений, по умолчанию config.ALLOWED_EXTENSION
    """

    ext = file.filename.split('.')[-1]
    if ext.lower() not in allowed_ext:
        raise HTTPException(
            status_code=400, detail='Неверный формат файла'
        )
