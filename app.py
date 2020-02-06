import flask
from flask import request
from werkzeug.utils import secure_filename
import os
from caption import caption_generator

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# app.config['UPLOAD_FOLDER'] = './media/'	

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET'])
def home():
    return "<h1>BE - Project</h1>"

@app.route('/upload', methods=['POST'])
def create_caption():
    target = os.path.join(APP_ROOT, 'media')
    image = request.files['image']

    destination = "/".join([target, image.filename])
    image.save(destination)


    return caption_generator(destination)

app.run()
