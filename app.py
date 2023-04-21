from flask import render_template

from flask import request
from flask_wtf.csrf import CSRFProtect

from wtforms import Form, TextAreaField, SubmitField, validators
import os

app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect()
csrf.init_app(app)



class ContactForm(Form):
    
    comment = TextAreaField('', [validators.DataRequired()])
    submit = SubmitField('Send')

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    
    form = ContactForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        return f'Sentiment : {}'
    
    return render_template('text.html', form=form)


