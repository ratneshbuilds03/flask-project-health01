import os
from dotenv import load_dotenv


load_dotenv()


def _resolve_database_url():
    existing_url = os.getenv("DATABASE_URL")
    if existing_url:
        return existing_url

    is_running_in_container = os.path.exists("/.dockerenv") or os.getenv("DOCKER_CONTAINER") == "1"
    host = "db" if is_running_in_container else "localhost"
    return f"mysql+pymysql://root:{os.getenv('MYSQL_ROOT_PASSWORD', 'Rm@12082003')}@{host}/task_manager_db"


class Config:
    SQLALCHEMY_DATABASE_URI = _resolve_database_url()
    SQLALCHEMY_TRACK_MODIFICATION = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
