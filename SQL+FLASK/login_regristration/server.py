from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'login_registration')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = '876dsf87ysuid'

@app.route('/')
def index():
    return render_template('index.html')

@app.sucess('/sucess', methods=['POST'])
def success():
    # pull data from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirm = request.form['confirm_password']

    #validate data and set error messages if needed
    errors = False
    if not first_name.isalpha() or len(first_name)<1:
        flash('name must contain no numbers and be at least 2 characters')
        errors = True
    if not last_name.isalpha() or len(last_name)<1:
        flash('name must contain no numbers and be at least 2 characters')
        errors = True
    if not EMAIL_REGEX.match(email): #false if not in proper format
        flash('invalid email format')
        errors = True
    if len(password) < 8:
        flash('password must be at least 8 characters')
        errors = True 
    if not password.match(password_confirm):
        flash("passwords don't match")
        errors = True

    # if errors - true redirect to index with flash messages
    if errors:
        return redirect('/')
    # else if valid submit to db redirect to index with flash success message promting login
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:fName, lName:, email, password, NOW(), NOW())"
        data = {
            'fName' : first_name,
            'lName' : last_name,
            'email' : email,
            'password': password
        }
        mysql.query_db(query, data)
        flash('successful registration, please login')
        return redirect ('/')

app.route('/user', methods=['POST'])
def login():
    # login data
    email = request.form['emal']
    password = request.form['password']

    #check if login info in db
    query = "SELECT * FROM users WHERE email = `email` and password = `password`(:email, :password)"
    print query
    data = {
        'email' : email,
        'password' : password
    }
    result = mysql.query_db(query, data)
    print result
    if len(result) > 0 #successfuly found a match in the db
        message = 'hello', result[0]['name']
        return render_template('user_page.html', greeting=message)
    else:
        flash("email and/or password invalid please try again")
        return redirect('/')

app.run(debug=True)
