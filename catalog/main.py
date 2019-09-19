from flask import Flask,redirect,url_for,render_template,request,flash
from flask_mail import Mail,Message
from random import randint 
from project_database import Register,Base,User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask_login import LoginManager,login_user,current_user,logout_user,login_required,UserMixin


#engine=create_engine('sqlite:///iii.db')
engine=create_engine('sqlite:///iii.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()

app = Flask(__name__)

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'




app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='ajaykumarmadhe044@gmail.com'
app.config['MAIL_PASSWORD']='ajaykumar#044'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.secret_key='abc'

mail=Mail(app)
otp=randint(000000,999999)
'''
@app.route("/Sample")
def demo():
	return"Hello World...Welcome to APSSDC"
@app.route("/demo")
def d():
	return "<h1> Hello .. This is Demo Page</h1>"
@app.route("/info/details")
def m():
	return "<h1>Hello Details..</h1>"
@app.route("/details/<name>/<int:age>/<float:salary>")
def info(name,age,salary):
	return"Hello ....This is {}.. My age is {} and My Salary is {}".format(name,age,salary)

@app.route("/admin")
def admin():
	return"Hello Admin"

@app.route("/student")
def student():
	return"Hello Student"

@app.route("/staff")
def staff():
	return"Hello Staff"

@app.route("/in/<name>")
def admin_info(name):
	if name=='admin':
		return redirect(url_for('staff'))
	else:
		return"No URL"

@app.route("/data/<name>/<int:age>/<float:salary>")
def demo_html(name,age,salary):
	return render_template('sample.html',n=name,a=age,s=salary) 

@app.route("/info-data")
def info_data():
	SNO=1
	Name="Ajay Kumar"
	Branch="CSE"
	Course="Python"
	return render_template('sample1.html',s_no=SNO,n=Name,b=Branch,c=Course)

data=[{'S_NO':123,'Name':'Ajay','Branch':'CSE','Course':'Python'},
{'S_NO':143,'Name':'Vijay','Branch':'CSE','Course':'HTML'}]

@app.route("/dummy")
def dummy_data():
	return render_template('sample2.html',dummy_info=data)

@app.route("/five/<int:number>")
def five_table(number):
	return render_template('sample3.html',n=number)

@app.route("/file_upload",methods=['GET','POST'])
def file_uploading():
	return render_template('file_upload.html')

@app.route("/success", methods=['GET','POST'])
def successful():
	if request.method=='POST':
		f=request.files['File']
		f.save(f.filename)

	return render_template("success.html",f_name=f.filename)

@app.route("/email", methods=['POST','GET'])
def email_send():
	return render_template("email.html")

@app.route("/email_verify", methods=['POST','GET'])
def verify_email():
	email=request.form['email']
	msg=Message("One Time Password",sender="ajaykumarmadhe044@gmail.com",recipients=[email])
	msg.body=str(otp)
	mail.send(msg)
	return render_template("v_email.html")

@app.route("/email_success", methods=['POST','GET'])
def success_email():
	user_otp= request.form['otp']
	if otp==int(user_otp):
		return render_template("email_success.html")
	return "Invalid OTP"

'''
@app.route("/")
def home():
    return render_template("Home.html")

		
@app.route("/show")
@login_required
def showdb():
	register=session.query(User).all()
	return render_template("show1.html",r=register)

@app.route("/New",methods=['POST','GET'])
def addData():
    if request.method=='POST':
        newData=User(name=request.form['name'],email=request.form['email'],password=request.form['password'])
        session.add(newData)
        session.commit()
        flash("New Data added....")
        return redirect(url_for('home'))
    else:
        return render_template("new.html")


@login_required
@app.route("/login",methods=['POST','GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('showdb'))

	try:
		if request.method=='POST':
			user=session.query(User).filter_by(email=request.form['email'],password=request.form['password']).first()	
			if user:
				login_user(user)
				return redirect(url_for('showdb'))
			else:
				flash("Invalid Login.....")	
		else:
			return render_template('login.html',title='login')
	except Exception as e:
		flash("Login Failed............")
	else:
		return render_template('login.html',title='login')		
@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))	
@login_manager.user_loader
def load_user(user_id):
	return session.query(User).get(int(user_id))					


@app.route("/edit/<int:register_id>",methods=['POST','GET'])
def editData(register_id):
    editedData=session.query(Register).filter_by(id=register_id).one()
    if request.method=='POST':
        editedData.name=request.form['name']
        editedData.surname=request.form['surname']
        editedData.mobile=request.form['mobile']
        editedData.email=request.form['email']
        editedData.branch=request.form['branch']
        editedData.role=request.form['role']
        editedData.password=request.form['password']
        session.add(editedData)
        session.commit()
        flash(" Data edited....")
        return redirect(url_for('showdb'))
    else:
        return render_template("edit.html",register=editedData)
        
    

@app.route("/delete/<int:register_id>",methods=['POST','GET'])
def deleteData(register_id):
    deletedData=session.query(Register).filter_by(id=register_id).one()
    if request.method=='POST':
        session.delete(deletedData)
        session.commit()
        flash("Data deleted....")
        return redirect(url_for('showdb'))
    else:
        return render_template('delete.html',register=deletedData)
        
@app.route("/account",methods=['POST','GET'])
@login_required
def account():
	return render_template("account.html")


if __name__=='__main__':
	app.run(debug=True)
