from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

def test_connection():
    application = create_app()
    with application.app_context():
        try:
            db.engine.connect()
            print("Success!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_connection()