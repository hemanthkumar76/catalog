from flask import Flask,redirect,url_for,render_template,request
from flask_mail import Mail,Message    #for email sending purpose
from random import randint
from project_database import Register,Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
app=Flask(__name__)
#app configuration for mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="hemanthkumariiitnuz@gmail.com"
app.config['MAIL_PASSWORD']="Hem@nth@#$76"
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=randint(000000,999999)
'''
@app.route("/sample")
def demo():
    
    return "Hello world"
@app.route("/demo")
def d():
    return "<h1>Hello Demo Page</h1>"

@app.route("/info/details")
def d1():
    return "Hello details"

#flask variables concept
@app.route("/details/<name>/<int:age>/<float:salary>")
def info1(name,age,salary):
    return "Name: {} age: {} salary: {}".format(name,age,salary)   


#url_for is used to redirect the page
@app.route("/admin")
def admin():
    return "Hello Admin"    

@app.route("/student")
def student():
    return "Hello student"   

@app.route("/staff")
def staff():
    return "Hello staff"  

@app.route("/info/<name>")
def info(name):
    if name=='admin':
        return redirect(url_for("admin"))    #redirect to admin function
    elif name=="student":
        return redirect(url_for("student"))
    elif name=="staff":
        return redirect(url_for("staff"))
    else:
        return "No url"
    
    
    
    
#adding html file to our app
        
@app.route("/data")
def add_html():
    return render_template('index.html')

#passing data to html page
@app.route("/data/<name>/<int:age>/<float:sal>")   
def passdata_template(name,age,sal):
    return render_template('index.html',n=name,a=age,s=sal)
          
@app.route("/data_to_html")   
def passdata1():
    sno=12
    name='hemanth'
    branch='cse'
    dept='rgukt'
    return render_template('index1.html',s_n=sno,n=name,b=branch,d=dept)
        
#multiple data passing
data=[{'sno':123,'name':'saral','branch':'IT','dept':'Training'},{'sno':124,'name':'hemanth','branch':'CSE','dept':'Training'}]        
@app.route('/dummy_data')
def dummy1():
    return render_template('index2.html',dummy_data=data)
        

#programming with flask printing table of a number
@app.route('/<int:number>')
def Table(number):
    return render_template('index3.html',n=number)
        
#file uploading concept
@app.route("/file_upload",methods=['GET','POST'])
def file_upload():
    return render_template("file_upload.html")

@app.route("/file",methods=['GET','POST'])
def success():
    if request.method=="POST":
        f=request.files['file']
        f.save(f.filename)
    return render_template("file.html",f_name=f.filename)de
    

'''

'''
@app.route("/email",methods=['POST','GET'])
def email_send():
    return render_template("email.html")


@app.route("/otp_verification",methods=['POST','GET'])
def validate_mail():
    email=request.form['email']
    msg=Message("Your OTP for verification of mail",sender="hemanthkumariiitnuz@gmai.com",recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template("v_email.html")

@app.route("/email_success",methods=["POST","GET"])
def success_email():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return render_template("email_success.html")
    return "Invalid OTP"
    
'''
@app.route("/show")
def showdb():
	register=session.query(Register).all()

	return render_template("show.html",reg=register)

@app.route("/New",methods=['POST','GET'])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],surname=request.form['surname'],mobile=request.form['mobile'],
			branch=request.form['branch'],role=request.form['role'])
		session.add(newData)
		session.commit()
		return redirect(url_for('showdb'))
	else:
		return render_template("new.html")



if __name__ == '__main__':
    app.run(debug=True)
