from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_marshmallow import Marshmallow # type: ignore
from flask_login import LoginManager # type: ignore
from flask_migrate import Migrate # type: ignore
from config import Config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.routes import bp as books_bp
    app.register_blueprint(books_bp, url_prefix='/api')

    return app