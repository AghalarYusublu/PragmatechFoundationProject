from flask import Flask,render_template,request,redirect

app=Flask(__name__)
city_list=[]
common_list=[]
id=1
cities=["Baki"]
@app.route('/',methods=['GET','POST'])
def index():
    global id    
    if request.method=='POST':
        mylist={
        'id':id,
        'name':request.form['ad'],
        'surname':request.form['soyad'],
        'email':request.form['email'],
        'city':request.form['city_select']
    }
        common_list.append(mylist)
        id+=1       
    return render_template('index.html',common_list=common_list,cities=cities)
   
@app.route('/addCity',methods=['GET','POST'])
def myCities(): 
    if request.method =='POST':
        cities.append(request.form['add_city'])
        return redirect('/')
    return render_template('addCity.html')

@app.route("/delete/<id>")
def delete(id):
    for mylist in common_list:
        if mylist['id']==int(id):
            common_list.remove(mylist)
            return redirect('/')
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)  