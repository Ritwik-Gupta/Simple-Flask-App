from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "testkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Tasks.sqlite"

from routes import *

db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run()
