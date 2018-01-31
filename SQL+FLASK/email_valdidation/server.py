from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_valid')

# variable for email valid regular expression check
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = 'one_life'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    # validate
    error = False
    error_message = 'Email is not valid!'
    if EMAIL_REGEX.match(request.form['email']):
        # write insert querry
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        # grab data from form
        data = {
            'email' : request.form['email']
        }
        #connect to mysql db
        mysql.query_db(query, data)

        # select all from db
        emails = mysql.query_db('SELECT * FROM users')
        return render_template('success.html', all_emails=emails)
    else:
        flash(error_message)
    return redirect('/')
    # if valid insert ito database

@app.route('/delete_user', methods=['POST'])
def user_delete():
    query = 'Delete FROM users ORDER BY id DESC limit 1 '
    mysql.query_db(query)
    
    return render_template('index.html')


app.run(debug=True)
