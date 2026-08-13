from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config
from app.utils.error_handlers import register_error_handlers


db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    register_error_handlers(app)
    
    from app.routes.task_routes import task_bp 
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)
    with app.app_context():
        from app.models.task import Task
        from app.models.user import User
        db.create_all()

    return app
    