from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
from datetime import datetime 

app = Flask(__name__)
mysql = MySQLConnector(app, 'login_registration')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = '876dsf87ysuid'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    # pull data from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    confirm_password = md5.new(request.form['confirm_password']).hexdigest()

    #trying to get dat formated when inserting into db
    # date = strftime("%B %d %Y")
    # print ('+++++++++++++')
    # print date
    # print ('+++++++++++++')

    #validate data and set error messages if needed
    errors = False
    if not first_name.isalpha() or len(first_name)<1:
        flash('first name must contain no numbers and be at least 2 characters')
        errors = True
    if not last_name.isalpha() or len(last_name)<1:
        flash('last name must contain no numbers and be at least 2 characters')
        errors = True
    if not EMAIL_REGEX.match(email): #false if not in proper format
        flash('invalid email format')
        errors = True
    if len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
        flash('password must be at least 8 characters')
        errors = True 
    if not password == confirm_password:
        flash("passwords don't match")
        errors = True

    # if errors - true redirect to index with flash messages
    if errors:
        return redirect('/')
    # else if valid submit to db redirect to index with flash success message promting login
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updatrd_at) VALUES (:fName, :lName, :email, :password, now(), now())"
        data = {
            'fName' : first_name,
            'lName' : last_name,
            'email' : email,
            'password': password,
            # 'date'  : date
        }
        mysql.query_db(query, data)
        flash('successful registration, please login')
        return redirect ('/')

@app.route('/user', methods=['POST'])
def login():
    # login data
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    #check if login info in db
    query = "SELECT first_name, last_name, DATE_FORMAT(created_at, '%W %M %e %Y') FROM users WHERE users.email = :email AND users.password = :password"
    data = {
        'email' : email,
        'password' : password
    }
    logedin_user = mysql.query_db(query, data)
    # created_at = logedin_user[0]['created_at']
    # print created_at
    # converted_date = strftime(createed_at, '%b')

    
    if len(logedin_user)>0:
        message = 'hello {}, welcome to your personal page. You created this account on: {}'.format(logedin_user[0]['first_name'], logedin_user[0]['created_at'])
        return render_template('user_page.html', greeting=message)
    else:
        flash("login failed: email and/or password invalid please try again")
        return redirect('/')

app.run(debug=True)
