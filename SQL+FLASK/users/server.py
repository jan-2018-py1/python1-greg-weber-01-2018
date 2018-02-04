from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re


app = Flask(__name__)
mysql = MySQLConnector(app, 'users')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = '876dsf87ysuid'

@app.route('/users')
def index():
    #query all users from db and store in a var
    query = 'Select id, CONCAT(first_name, ' ', last_name) as full_name, email, created_at FROM users)'
    users = mysql.query_db(query)
    #render all users in a table with links to -new user, edit user, show user, delete user
    return render_template('index.html', users=users)


@app.route('/users/new')
def new():
    # render form to add new user
    return render template('users_new.html')


@app.route("/users/<session['u_id']>/edit")
def edit():
    # render form to edit profile based on logged-in user
    return render_template('users_edit.html')


@app.route("/users/<session['u_id']>")
def show():
    #display user profile using sessions['u_id'] us reference
    return render_template('user_show.html')


@app.route('/users/create', methods=['POST'])
def create():
    # pull info from new user form and insert into db
    returnb redirect("/users/<session['u_id']>")


@app.route("/user/<session['u_id']>/destroy")
def detroy():
    # delete given user by id from db
    return redirect('/users')


@app.route("user/update/<session['u_id']>")
def update():
    # update query info in user profile on db with info rom form on user edit page
    return redirect("/users/<session['u_id']>")


app.run(debug=True)