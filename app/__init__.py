from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/user_login'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect()
csrf.init_app(app)

from app import models

with app.app_context():
    db.create_all()

from app import routes