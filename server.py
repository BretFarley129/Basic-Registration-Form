from flask import Flask, request, redirect, render_template, session, flash
import re
import md5

app = Flask(__name__)
app.secret_key = "waow"

@app.route('/')
def index():
    session["loggedOn"] = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():

    #get data from forms
    first = request.form['firstName']
    last = request.form['lastName']
    email = request.form['email']
    password = request.form['password']
    hashed_password = md5.new(password).hexdigest()
    confirm = request.form['confirm']
    
    
    properLogin = True
    if len(first) < 3:
        flash("first name must be at least 2 letters long")
        properLogin = False

    if len(last) < 3:
        flash("last name must be at least 2 letters long")
        properLogin = False

    my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    check = "SELECT * FROM users"
    if not my_re.match(email):
        flash("please use a proper email")
        properLogin = False
    
    if len(password) < 8:
        flash("password must be at least 8 characters long")
        properLogin = False
    if password != confirm:
        flash("passwords must match")
        properLogin = False
    
    if properLogin:
        flash("Welcome to this pointless website {} {}!".format(first, last))
        return redirect('/')
    else:
        return redirect('/')

        
    

app.run(debug=True)
