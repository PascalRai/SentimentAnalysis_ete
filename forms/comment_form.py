from flask_wtf.csrf import CSRFProtect
from wtforms import Form, TextAreaField, SubmitField, validators

class ContactForm(Form):
    comment = TextAreaField('', [validators.DataRequired()])
    submit = SubmitField('Send')