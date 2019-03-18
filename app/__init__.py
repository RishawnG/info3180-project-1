from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)







app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1db"
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
db = SQLAlchemy(app)
from app import views