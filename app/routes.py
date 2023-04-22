from app import app
from flask import render_template
from flask import request
from app.utils.prediction import predict
from app.forms import ContactForm

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    
    form = ContactForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        return f'Sentiment : {predict(form.comment.data)}'
    
    return render_template('text.html', form=form)