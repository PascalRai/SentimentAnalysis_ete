from wtforms import Form, TextAreaField, SubmitField, validators

class ContactForm(Form):
    comment = TextAreaField('', [validators.DataRequired()])
    submit = SubmitField('Send')