import os

class Config:
    SECRET_KEY = "supersecretkey"  # Можно заменить на os.environ.get("SECRET_KEY")
    UPLOAD_FOLDER = os.path.join("static", "images")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
