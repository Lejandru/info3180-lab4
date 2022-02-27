from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import Flask
from werkzeug.utils import secure_filename



class UploadForm(FlaskForm):
    imageFile = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Appropriate Images Only')])