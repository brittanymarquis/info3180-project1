from flask_wtf.file import FileAllowed, FileRequired, FileField
from flask_wtf import FlaskForm

class UploadForm(FlaskForm):
      upload = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Only jpg, png and jpeg is accepted')])
