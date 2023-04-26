from app import db
from flask_login import login_user, LoginManager, login_required, UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
