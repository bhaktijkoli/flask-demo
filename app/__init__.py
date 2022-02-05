from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv

load_dotenv()

# APP
app = Flask(os.getenv("FLASK_SERVER_NAME", __name__))
# DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///db.sqlite3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
# ROUTES
from app.routes import index
from app.routes.users import users

app.register_blueprint(users)

# BOOT
from app.boot import boot

boot()
