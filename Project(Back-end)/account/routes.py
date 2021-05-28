from app import app 
from app.models import *
from app import db
from flask import render_template,redirect,request,url_for




@app.route("/register/")
def register():
    return render_template('account/register.html')