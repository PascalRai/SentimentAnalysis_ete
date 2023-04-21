from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

from app import views

app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect()
csrf.init_app(app)