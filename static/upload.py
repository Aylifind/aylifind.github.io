from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
import pickle
from skimage.io import imread
import numpy as np


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():

    data = {
        "lost_or_found" : request.form.get('lost_found'),
        "pet" : request.form.get('pet'),
        "location" : request.form.get('location'),
        "date" : request.form.get('date'),
        "color" : request.form.get('color'),
        "addit_info" : request.form.get('addit_info')
        }

    files = request.files.getlist('files[]')
    file_num = 0
    for file in files:
        file_num += 1
        image = imread(file)
        data['file_{}'.format(file_num)] = image

    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    return redirect(url_for('read_results'))


def make_similarity_search():
    pass


@app.route('/result', methods=['POST', 'GET'])
def read_results():

    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    data['lost_or_found'] = 'Changed' 
    return '''
           <h2>Changed</h2>
           {}
           '''.format(data['lost_or_found'])





if __name__ == '__main__':
    app.run(debug=True)
