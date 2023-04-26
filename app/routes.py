from flask_login import login_user, LoginManager, login_required, UserMixin
from google_auth_oauthlib import get_user_credentials
from app import db
from app import app
from flask import render_template
from flask import request
from flask import redirect
from app.models import User
from app.utils.prediction import predict
from app.forms import *

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    
    form = ContactForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        temp = predict(form.comment.data)
        return f'Sentiment : {temp[0]} with probability of {str(temp[1])}'
    
    return render_template('text.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = (form.email.data, form.name.data, form.password1.data, form.password2.data)
        user = User(request.form['email'], request.form['name'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        print('User created successfully!')
        return redirect('/login/')
    else:
        print('Error!')
        return render_template('register.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        print('Done1')
        if user:
            print('Done2')
            if user.password == form.password.data:
                print('Done3')
                login_user(user)
        # password = request.form['password']
        
        # user = User.query.filter_by(email=email)

        # if user is not None:
        #     login_user(user)
        #     return redirect('/')


        # if user is not None:
        #     login_user(request,user)
        # return redirect('/')
    else:
        print('Error')
        return render_template('login.html', form=form)