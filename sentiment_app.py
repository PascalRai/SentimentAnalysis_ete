from flask import Flask, render_template
import numpy as np
import pickle
import tensorflow as tf

from flask import request
# from flask_wtf.csrf import CSRFProtect

from wtforms import Form, TextAreaField, SubmitField, validators

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)

vocab_size = 100_000
max_len = 55

model = tf.keras.models.load_model('sentiment_model.h5')
le = pickle.load(open('le_model.sav', 'rb'))
data = np.load('vocab.npz')
vocab = data['arr_0']

vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=vocab_size,
    output_mode='int',
    standardize='lower_and_strip_punctuation',
    output_sequence_length=max_len,
    vocabulary = vocab
)

class ContactForm(Form):
    
    comment = TextAreaField('', [validators.DataRequired()])
    submit = SubmitField('Send')

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    
    form = ContactForm(request.form)
    
    if request.method == 'POST' and form.validate():
    
        text_comment = form.comment.data
        y = vectorize_layer([text_comment])
        y = model.predict(y)
        y = np.argmax(y,axis=1)
        
        return f'Sentiment : {le.inverse_transform(y)[0]}'
    
    return render_template('text.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
