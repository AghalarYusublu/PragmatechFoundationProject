from flask import Flask,flash,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataForm.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    f_name=db.Column(db.String(100))
    l_name=db.Column(db.String(100))
    user_name=db.Column(db.String(100))
    email=db.Column(db.String(200))
    adress=db.Column(db.String(300))
    adress_2=db.Column(db.String(300))
    country=db.Column(db.String(200))
    state=db.Column(db.String(200))
    zip=db.Column(db.Integer)
    checkbox=db.Column(db.String(100))
    customRadio=db.Column(db.String(100))
    card_name=db.Column(db.String(200))
    card_num=db.Column(db.Integer)
    expiration=db.Column(db.Integer)
    cvv=db.Column(db.Integer)

class Country(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    country_name=db.Column(db.String(200))
    states=db.relationship('State', backref='country', lazy=True)

class State(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    state_name=db.Column(db.String(200))
    country_id=db.Column(db.Integer, db.ForeignKey('country.id'),  nullable=False)



@app.route('/',methods=['GET','POST'])
def index():      
    users=User.query.all()
    return render_template('index.html',users=users)

@app.route('/add',methods=['GET','POST'])
def add():
    countries=Country.query.all()
    states=State.query.all()
    if request.method=='POST':
        user=User(
            f_name=request.form['f_name'],
            l_name=request.form['l_name'],
            user_name=request.form['user_name'],
            email=request.form['email'],
            adress=request.form['adress'],
            adress_2=request.form['adress_2'],
            country=request.form['country'],
            state=request.form['state'],
            zip=request.form['zip'],
            checkbox=request.form['checkbox'],
            customRadio=request.form['customRadio'],
            card_name=request.form['card_name'],
            card_num=request.form['card_num'],
            expiration=request.form['expiration'],
            cvv=request.form['cvv']     
        )  
        db.session.add(user)
        db.session.commit()   
        return redirect('/')
     
    return render_template('add.html',countries=countries,states=states)

@app.route("/delete/<id>",methods=['GET','POST'])
def delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')



@app.route("/update/<id>",methods=['GET','POST'])
def update(id):
    user=User.query.get(id)
    countries=Country.query.all()
    states=State.query.all()
    if request.method=='POST':
        user.f_name=request.form['f_name']
        user.l_name=request.form['l_name']
        user.user_name=request.form['user_name']
        user.email=request.form['email']
        user.adress=request.form['adress']
        user.adress_2=request.form['adress_2']
        user.country=request.form['country']
        user.state=request.form['state']
        user.zip=request.form['zip']
        user.checkbox=request.form['checkbox']
        user.customRadio=request.form['customRadio']
        user.card_name=request.form['card_name']
        user.card_num=request.form['card_num']
        user.expiration=request.form['expiration']
        user.cvv=request.form['cvv'] 
        db.session.merge(user)
        db.session.flush() 
        db.session.commit()
        return redirect('/')      
    return render_template('update.html',user=user,countries=countries,states=states)

@app.route("/country/add",methods=['GET','POST'])
def add_country():  
    if request.method=='POST':
        country=Country(
            country_name=request.form['country_name']
        )
        db.session.add(country)
        db.session.commit()
        return redirect('/add')
    return render_template('add_country.html')

@app.route("/state/add",methods=['GET','POST'])
def add_state():  
    countries=Country.query.all()
    if request.method=='POST':
        state=State(
            state_name=request.form['state_name'],
            country_id=int(request.form['country'])
        )
        db.session.add(state)
        db.session.commit()
        return redirect('/add')
    return render_template('add_state.html',countries=countries)



if __name__ == '__main__': 
    app.run(port=5000,debug=True)