from pathlib import Path

from apiflask import APIFlask
from apispec_oneofschema import MarshmallowPlugin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
marsh = Marshmallow()


def create_app():
    app = APIFlask(__name__, title="DRY API", version="1.0", docs_ui="elements", spec_plugins=[MarshmallowPlugin()])
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{Path(__file__).parent.absolute()}/database.db"

    db.init_app(app)
    with app.app_context():
        db.create_all()
    marsh.init_app(app)

    return app
