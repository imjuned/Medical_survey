import os 
from flask import Flask
from flask import render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask import flash

# basedir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the random string'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/medical'



db = SQLAlchemy(app)

class admindash(db.Model):
    __tablename__="admindash"
    user_name = db.Column(db.String(50),primary_key=True)
    pass_w = db.Column(db.Integer)

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
        data1 = admindash.query.all()
        print(data1)
        for i in data1:
            if i.user_name==User and i.pass_w==password:
                return redirect('/admin/dashboard')
                    # print("redited")
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
    # # if ()
    # #     if 
    #     return(redirect(url_for('/Hospital/Dashboard')))

    return render_template('/hospital/signin.html')

@app.route('/signup')
def signup():
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

if __name__=='__main__':
    app.run(debug=True)