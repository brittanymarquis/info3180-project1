from Flask import Flask

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)

#configuartion uploads
UPLOAD_FOLDER = './app/static/uploads'
upload_f=app.config['UPLOAD_FOLDER']
Allowed_uploads=['png','jpg']


app.config.from_object(__name__)
from app import views
