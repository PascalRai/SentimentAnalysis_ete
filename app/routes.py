from app import app
from flask import render_template
from flask import request
from app.utils.prediction import predict
from app.forms import ContactForm

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    
    form = ContactForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        temp = predict(form.comment.data)
        return f'Sentiment : {temp[0]} with probability of {str(temp[1])}'
    
    return render_template('text.html', form=form)