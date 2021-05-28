from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import lazyload



app=Flask(__name__)
upload_folder='app/static/uploads/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ProjectDatabase.db'
app.config['UPLOAD_FOLDER']=upload_folder 
app.config['SECRET_KEY']='mysecretkey'

db = SQLAlchemy(app)
migrate=Migrate(app,db)

from app.models import * 
from admin.routes import *
from main.routes import *   

# db.create_all()