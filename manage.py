import os 
from flask import Flask
from flask import render_template,request,redirect,url_for
from flask_mysqldb import MySQL

from flask_sqlalchemy import SQLAlchemy
from flask import flash


# basedir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/medical'

app.config['SECRET_KEY'] = 'the random string'

db = SQLAlchemy(app)

def dbconn_ad(user,password):
    if user=='admin1' and password=='123456':
        return True
    return False
#admin Data base
#Data Base goes here

class admindash(db.Model):
    __tablename__="admindash"
    user_name = db.Column(db.String(50),primary_key=True)
    pass_w = db.Column(db.Integer)


class hospitaldb(db.Model):
    __tablename__="hospitaldb"
    hospital_name = db.Column(db.String(50))
    incharge_name = db.Column(db.String(50))
    email = db.Column(db.String(50),primary_key=True)
    mobile = db.Column(db.Integer)
    user_n = db.Column(db.String)
    pssword = db.Column(db.String(18))


class patientdetail(db.Model):
    __tablename__="patientdetail"
    Name = db.Column(db.String(50))
    aadhar= db.Column(db.String(50),primary_key=True)
    mobile = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    address = db.Column(db.String(50))
    state = db.Column(db.String(50))
    Taluqa = db.Column(db.String(50))
    zipcode =  db.Column(db.String(50))
    
class patientknown(db.Model):
    __tablename__="patientknown"
    uid = db.Column(db.String(50),primary_key=True)
    Dieasename = db.Column(db.String(50))
    other = db.Column(db.String(50))
    traveltime = db.Column(db.Integer)
    
class patientunknown(db.Model):
    __tablename__="patientunknown"
    uid = db.Column(db.String(50),primary_key=True)
    symptoms = db.Column(db.String(50))
    
#Tables End here

@app.route('/admin',methods=['GET','POST'])
def admin():
    if (request.method=='POST'):
        User = request.form.get('user')
        password = request.form.get('password')
        # # print(User)
        # # print(password)#for regiy
        # entry = admindash(user_name=User,pass_w=password)
        # db.session.add(entry)
        # db.session.commit()
        # print("Successful!")
        # # print(password,User)
        # data1 = admindash.query.filter_by(user_name='admin1').first()
        # i=data1[1].pass_w
        # print(data1)
        if (dbconn_ad(User,password)):
            return redirect('/admin/dashboard')
        else:
            flash("some text to flash")
    print('nothinghapped')
    return render_template('/admin/login.html')

    # return render_template('/admin/login.html')


# Home page 
@app.route('/')
def login():
    # print("hello")
    return render_template('index.html')
# home page connected to sigin 
# that route will denote whatcustom url you want to make 
# you have to mention that same in anchor tag just /url not file loaction
#and for routing as usual

@app.route('/signin')
def signin():
    if (request.method=='POST'):
        user = request.form.get('usernameh')
        password = request.form.get('passwordh')
        print(user,password)
        data = hospitaldb.query.all()
        print(data)
        for i in data:
            print(data)
            if data.i.hospital_name==user and i.data.pssword==password:
                return(redirect(url_for('/Hospital/Dashboard')))

        
    # # if ()
    # #     if 
    #     return(redirect(url_for('/Hospital/Dashboard')))

    return render_template('/hospital/signin.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if (request.method=='POST'):
        nameh=0
        nameh = request.form.get('name')
        incharge = request.form.get('inchargename')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        user = request.form.get('usern')
        password = request.form.get('password')
        
        # # print(User)
        entry = hospitaldb(hospital_name=nameh,incharge_name=incharge,email=email,mobile=mobile,user_n=user,pssword=password)
        db.session.add(entry)
        db.session.commit()
        
        return redirect('/signin')

    return render_template('/hospital/signup.html')

@app.route('/hospital/Dashboard')
def dashboard():
    data = {
        'Dieases':['Allergies','Colds and Flu','Conjunctivitis ("pink eye“)','Diarrhea','Headaches','Mononucleosis','Stomach','Aches','Allergies','Aches'],
        'PatientID':[12345678,12345678,12345678,12345678,12345678,12345678,12345678,12345678,12345678,12345678],
        'Place':['Nanded','Nanded','Nanded','Nanded','Nanded','Nanded','Nanded','Nanded','Nanded','Nanded'],
        'status':['known','known','known','known','known','known','known','known','known','known']
    }


    return render_template('/hospital/hospitaldash.html',data=data)

@app.route('/hospital/AddPatient')
def addpatient():
    return render_template('/hospital/addPateint.html')

@app.route('/hospital/commondisease')
def commondiease():
    
    # pass
    return render_template('/hospital/commondisease.html')

@app.route('/hospital/unknown')
def unknown():
    return render_template('/hospital/unknown.html')



@app.route('/admin/dashboard')
def adminView():
    data = {
        # Diarrhea.Headaches.Mononucleosis.Stomach Aches.
        'Hopital_Name':['Apex','Apolo','MaxHopital','Lotus'],
        'Patients_Count':[40,100,80,50],
        'Area':['Nanded','Nanded','Nanded','Nanded'],
        # 'Status':['-','-','known','known']
    }
    return render_template('/admin/admindash.html',data=data)
@app.route("/logout")
def logout():
    return redirect('/')


@app.route("/table")
def readtable():
    data = admindash.query.all()
    print(type(data))
    print(data)
    return render_template("/hospital/table.html", data = data)


if __name__=='__main__':
    app.run(debug=True)