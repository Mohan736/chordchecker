import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask.blueprints import Blueprint
from models.ApiMessage import ApiMessage,MessageType
from services.ChordChecker import ChordChecker
from pathlib import Path
import uuid
# from flask import current_ap

upload = Blueprint('upload', __name__, template_folder='templates')


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav'}
# ALLOWED_EXTENSIONS = {'wav'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload.route('/api/file-upload', methods=['GET', 'POST'])
def upload_file():
    res = 'Bad request method'
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('Empty file')
            res = 'Empty file'
        chord = request.form.get('chord')  
        print("Selected chord: "+chord)  
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            # flash('No selected file')
            res = 'No selected file'
        if file and allowed_file(file.filename):
            
            file_name = str(uuid.uuid4())
            name = file_name+'.wav'
            filename = secure_filename(name)
            # file.save(os.path.join(current_ap.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # start process
            checker = ChordChecker(os.path.join(UPLOAD_FOLDER, filename), chord)
            res = checker.processCheck(2)
            os.remove(os.path.join(UPLOAD_FOLDER, filename))
            # flash(res)
        else:
            res = 'Wrong file: upload a valid file (wav format)'    
        
    return res
