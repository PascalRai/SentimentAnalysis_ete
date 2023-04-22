import numpy as np
import pickle
import tensorflow as tf
import os

vocab_size = 100_000
max_len = 55

dir_path = os.path.dirname(os.path.realpath(__file__))

le = pickle.load(open(os.path.join(dir_path, 'le_model.sav'), 'rb'))
model = tf.keras.models.load_model(os.path.join(dir_path, 'sentiment_model.h5'))
data = np.load(os.path.join(dir_path,'vocab.npz'))
vocab = data['arr_0']

vectorize_layer = tf.keras.layers.TextVectorization(
    max_tokens=vocab_size,
    output_mode='int',
    standardize='lower_and_strip_punctuation',
    output_sequence_length=max_len,
    vocabulary = vocab
)

def predict(comment):
    y = vectorize_layer([comment])
    y = model.predict(y)
    y = np.argmax(y,axis=1)
    y = le.inverse_transform(y)[0]
    return y