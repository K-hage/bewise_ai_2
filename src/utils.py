from pathlib import Path

from src.config import BASE_DIR, STORAGE_PATH


async def create_folder(base_dir: str = BASE_DIR, folder: str = STORAGE_PATH) -> None:
    """
    Создает директорию для файлов если она отсутствует
    :param base_dir: директория проекта
    :param folder: директория для файлов
    :return:
    """

    path = Path(base_dir) / folder
    if not path.is_dir():
        path.mkdir(parents=True, exist_ok=True)
