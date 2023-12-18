from pathlib import Path

from apiflask import APIFlask
from apispec_oneofschema import MarshmallowPlugin
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# Local Imports
from plugins.titles_plugin import TitlesPlugin

db = SQLAlchemy()
marsh = Marshmallow()


def create_app():
    app = APIFlask(
        __name__,
        title="DRY API",
        version="1.0",
        docs_ui="swagger-ui",
        spec_plugins=[MarshmallowPlugin(), TitlesPlugin()],
    )
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{Path(__file__).parent.absolute()}/database.db"
    app.config["AUTO_SERVERS"] = False
    app.servers = [
        {
            "name": "Production Server",
            "url": "https://dry-apiflask-demo-r5uz5svela-uc.a.run.app",
        },
    ]

    db.init_app(app)
    with app.app_context():
        db.create_all()
    marsh.init_app(app)

    CORS(app, origins="*")

    return app
