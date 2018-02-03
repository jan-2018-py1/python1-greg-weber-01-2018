from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
import md5


app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = '876dsf87ysuid'

@app.route('/')
def index():
    if 'uid' in session:
        return redirect ('/wall')
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    # take in info from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    confirm_password = md5.new(request.form['confirm_password']).hexdigest()

    #run validations
    reg_errors = False
    if not first_name.isalpha() or len(first_name)<2:
        flash('first name must contain no numbers and be at least 2 characters')
        reg_errors = True
    if not last_name.isalpha() or len(last_name)<2:
        flash('last name must contain no numbers and be at least 2 characters')
        reg_errors = True
    if not EMAIL_REGEX.match(email): #false if not in proper format
        flash('invalid email format')
        reg_errors = True
    if len(request.form['password']) < 8 or len(request.form['confirm_password']) < 8:
        flash('password must be at least 8 characters')
        reg_errors = True 
    if password != confirm_password:
        flash("passwords don't match")
        reg_errors = True
    
    # if valid insert info into db and login user to session - redirect to wall/ if not redirect to index
    if reg_errors:
        session['red_class'] = 'red'
        return redirect('/')
    # else if valid submit to db redirect to index with flash success message promting login
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:fName, :lName, :email, :password, now(), now())"
    data = {
        'fName' : first_name,
        'lName' : last_name,
        'email' : email,
        'password': password,
    }
    new_user = mysql.query_db(query, data)
    session['uid'] = new_user
    session['first_name'] = first_name
    return redirect('wall')

@app.route('/login', methods=['POST'])
def login():
    #check user input against db - login to sessions if sussessful and redirect to '/wall', else redirect to root
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    #chek against db
    query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
    data = {
        'email' : email,
        'password' : password
    }
    user = mysql.query_db(query, data)
    
    if len(user) == 0:
        flash('email & password not found please try again or register as new user')
        session['red_class'] = 'red'
        return redirect('/')
    session['uid'] = user[0]['id']
    session['first_name'] = user[0]['first_name']
    return redirect('wall')


@app.route('/wall')
def wall_display():
    if 'uid' not in session:
        return redirect('/')
    #querry all posts/comments and render 'wall.html'- most recent post first, oldest comment first
    query = "select posts.id as post_id, users.first_name, posts.content, DATE_FORMAT(posts.created_at, '%W %M %e %Y') as created_at FROM users JOIN posts ON users.id = posts.user_id ORDER BY  posts.created_at DESC"
    posts = mysql.query_db(query)
    print '--'*50
    print posts[0]
    print '--'*50
    return render_template('wall.html', posts=posts)




@app.route('/posts', methods=['POST'])
def post():
    if 'uid' not in session:
        return redirect('/')
    #grab post text from wall form and insert into db redirect to wall
    post_message = request.form['post']
    query = 'INSERT INTO posts (user_id, content, created_at, updated_at) VALUES (:uid, :content, NOW(), NOW())'
    data = {
        'uid' : session['uid'],
        'content' : post_message
    }
    post_message_id = mysql.query_db(query, data)  #not sure if I will need the id returned from the insert but will grab incase 

    return redirect('/wall')




@app.route('/comment', methods=['POST'])
def comment():
    if 'uid' not in session:
        return redirect('/')
    comment = request.form['comment']
    print comment
    post_id = request.form['post_id']
    print post_id
    # print '--'*50
    # print post_id
    # print '--'*50
    # # grab comment text and insert into db - redirect to wall

  


    return redirect('/wall')



@app.route('/delete', methods=['POST'])
def delete():
    if 'uid' not in session:
        return redirect('/')
    #add delet button to comments - if delete button pushed - check uid against comment id -allow delete if match delete from db - redirect to wall
    #maybe flash a message saying 'you can only delete your own posts' if user id doesent match comment user id
   
   
    return redirect('/wall')


@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")

app.run(debug=True)