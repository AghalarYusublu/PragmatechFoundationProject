# main routes
from app import app 
from app.models import Orders
from app import db

from flask import render_template,redirect,request,url_for


@app.route("/")
def main():
    return render_template('main/index.html')


@app.route("/orders/",methods=['GET','POST'])
def orders():
    if request.method=='POST':
        order=Orders(
            package_name=request.form['package_name'],
            email=request.form['email'],
            phone=request.form['phone'],
            comment=request.form['comment'],
            complete_order_btn=request.form['complete_order_btn'],
            foodpackage_id=request.form['package_name']
        )
        db.session.add(order)
        db.session.commit()  
        return redirect(url_for('main'))
    return render_template('main/index.html')


@app.route('/orders/delete/<id>',methods=['GET','POST'])
def orders_delete(id):
    order=Orders.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('admin_tables'))