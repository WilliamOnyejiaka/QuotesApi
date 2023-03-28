from flask import Flask
from .api.v1.routes.quotes import quotes
from .api.v1.routes.admin import admin
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app, supports_credentials=True, resources={
        r"/*": {
            "origins": {
                "*",
            }
        }
    })

    app.register_blueprint(quotes)
    app.register_blueprint(admin)

    return app
