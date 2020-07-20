import os
import io
from flask import Flask, request, send_from_directory, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid

from app.ml.main import convertToAnime

app = Flask(__name__, static_folder="", static_url_path="")

PreConvertFolder = './app/ml/dataset/cat2anime/'
PostConvertFolder = './app/ml/results/cat2anime/test/'

CORS(app)

@app.route('/uploadImage', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    newfilename = str(uuid.uuid4()) 

    # Make a directory
    newdirectory = os.path.join(PreConvertFolder, newfilename)
    os.mkdir(newdirectory)

    newlocation = os.path.join(newdirectory, newfilename + '.' + filename.split('.')[-1] )
    file.save(newlocation)
    # Check File Exist
    fileExist = checkfile(newlocation)
    if fileExist:
        convertImage(newlocation, newfilename)
        return newfilename + '.png'
    else:
        return abort(Response('File Not Exist'))

def checkfile(location):
    return os.path.exists(location)

def convertImage(newlocation, newfilename):
    convertToAnime(newlocation, newfilename)
    return 

@app.route('/downloadImage/<filename>', methods=['GET'])
def download(filename):
    with open(os.path.join(PostConvertFolder, filename), 'rb') as bites:
        return send_file(
            io.BytesIO(bites.read()),
            mimetype="image/png"
        )
    