import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = bool(int(os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]))
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello!"