import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from sqlalchemy.exc import OperationalError

from app.config import Config
from app.utils.error_handlers import register_error_handlers


db = SQLAlchemy()
jwt = JWTManager()


def _create_tables_with_retry(max_retries=30, delay=2):
    for attempt in range(1, max_retries + 1):
        try:
            db.create_all()
            return
        except OperationalError as exc:
            message = str(exc).lower()
            if "can't connect to mysql server" not in message and "connection refused" not in message:
                raise
            if attempt == max_retries:
                raise
            time.sleep(delay)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    register_error_handlers(app)

    from app.routes.task_routes import task_bp
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(task_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api')

    with app.app_context():
        from app.models.task import Task
        from app.models.user import User
        _create_tables_with_retry()

    return app
    