from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent.parent

if (env_path := BASE_DIR.joinpath('.env')) and env_path.is_file():
    env.read_envfile(env_path)

# Database
DB_HOST = env.str('DB_HOST')
DB_PORT = env.str('DB_PORT')
DB_NAME = env.str('DB_NAME')
DB_USER = env.str('DB_USER')
DB_PASSWORD = env.str('DB_PASSWORD')

# file storage
STORAGE_PATH = env.str('STORAGE_PATH', default='temp')

# extension upload
ALLOWED_EXTENSION = env.list(
    'ALLOWED_EXTENSION',
    default=[
        'wav',
    ]
)
