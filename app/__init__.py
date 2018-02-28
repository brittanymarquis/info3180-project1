from flask import Flask

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = './app/static/uploads'


#configuartion uploads
app = Flask(__name__)
app.config.from_object(__name__)
upload_f=app.config['UPLOAD_FOLDER']
Allowed_uploads=['png','jpg']


app.config.from_object(__name__)
from app import views
