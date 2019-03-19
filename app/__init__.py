from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)







app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/Project1DB"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://jbxzounbbrbyuh:05b46786c0e2ed21bfcd58674214e86ffe7affca58472e4361ff6dafde73c897@ec2-75-101-133-29.compute-1.amazonaws.com:5432/d6udi20aaehfrd'
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)
from app import views