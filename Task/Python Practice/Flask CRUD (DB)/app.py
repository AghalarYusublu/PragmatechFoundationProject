from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Worker(db.Model):
    id=db.Column(db.Integer,primary_key= True)
    f_name=db.Column(db.String(50))
    l_name=db.Column(db.String(50))
    age=db.Column(db.Integer)
    email=db.Column(db.String(100))
    city=db.Column(db.String(100))



@app.route('/',methods=['GET','POST'])
def index(): 
    workers=Worker.query.all()
    return render_template('index.html',workers=workers)
    

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        worker=Worker(
            f_name=request.form['f_name'],
            l_name=request.form['l_name'],
            age=request.form['age'],
            email=request.form['email'],
            city=request.form['city_select']
        )
        db.session.add(worker)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')
  
  

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    worker=Worker.query.get(id)
    if request.method=='POST':
        worker.f_name=request.form['f_name']
        worker.l_name=request.form['l_name']
        worker.age=request.form['age']
        worker.email=request.form['email']
        worker.city=request.form['city_select']
        db.session.commit()
        return redirect('/')
    return render_template('update.html',worker=worker)

@app.route('/delete/<id>',methods=['GET','POST'])
def delete(id):
    worker=Worker.query.get(id)
    db.session.delete(worker)
    db.session.commit() 
    
    return redirect('/')


db.create_all()
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
