from flask import Flask
from flask import render_template,request,redirect,url_for

app = Flask(__name__)
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
    return render_template('hdashboard.html')

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

@app.route('/admin')
def admin():
    return render_template('/admin/login.html')

@app.route('/admin/dashboard')
def adminDash():
    return render_template('/admin/dashboard.html')

if __name__=='__main__':
    app.run(debug=True)