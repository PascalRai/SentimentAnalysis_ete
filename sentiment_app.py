from flask import Flask, render_template

from flask import request
# from flask_wtf.csrf import CSRFProtect

from wtforms import Form, TextAreaField, SubmitField, validators

# import os

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)

class ContactForm(Form):
    
    comment = TextAreaField('', [validators.DataRequired()])
    submit = SubmitField('Send')

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    
    form = ContactForm(request.form)
    
    if request.method == 'POST' and form.validate():
    
        text_comment = form.comment.data
        
        return 'Sentiment : positive'
    
    return render_template('text.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
