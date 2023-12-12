from pathlib import Path

from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = APIFlask(__name__, title="DRY API", version="1.0")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).parent.absolute()}/database.db"

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
