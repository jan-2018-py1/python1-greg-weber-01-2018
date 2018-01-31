from flask import Flask, redirect, render_template, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
    friends = mysql.query_db('SELECT name, age, created_at FROM friends')
    return render_template('index.html', all_friends=friends)

@app.route('/new_friend', methods=['POST'])
def new_friend():
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
        'name' : request.form['name'],
        'age'  : request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)