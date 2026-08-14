import os
from dotenv import load_dotenv


load_dotenv()


def _resolve_database_url():
    # Check for external database URL first (for production)
    existing_url = os.getenv("DATABASE_URL")
    if existing_url:
        # Convert postgres URL to mysql if needed
        if existing_url.startswith("postgres"):
            existing_url = existing_url.replace("postgres://", "mysql+pymysql://")
        return existing_url

    # For Docker containers
    is_running_in_container = os.path.exists("/.dockerenv") or os.getenv("DOCKER_CONTAINER") == "1"
    
    if is_running_in_container:
        host = "db"
    else:
        host = os.getenv("MYSQL_HOST", "localhost")
    
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_ROOT_PASSWORD", "Rm@12082003")
    database = os.getenv("MYSQL_DATABASE", "task_manager_db")
    
    return f"mysql+pymysql://{user}:{password}@{host}/{database}"


class Config:
    SQLALCHEMY_DATABASE_URI = _resolve_database_url()
    SQLALCHEMY_TRACK_MODIFICATION = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")
