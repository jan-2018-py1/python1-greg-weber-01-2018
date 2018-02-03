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
    if 'u_id' in session:
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

    # if not valid redirect to index
    if reg_errors:
        session['red_class'] = 'red'
        return redirect('/')
    # else if valid insert intto db and redirect to wall
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:f_name, :l_name, :email, :password, now(), now())"
    data = {
        'f_name' : first_name,
        'l_name' : last_name,
        'email' : email,
        'password': password,
    }
    new_user = mysql.query_db(query, data)
    session['u_id'] = new_user
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
    session['u_id'] = user[0]['id']
    session['first_name'] = user[0]['first_name']
    return redirect('wall')


@app.route('/wall')
def wall_display():
    if 'u_id' not in session:
        return redirect('/')
    #querry all posts and store in []
    posts_query = "SELECT users.id as poster_user_id, users.first_name as poster_name, posts.content as post, posts.id as post_id, DATE_FORMAT(posts.created_at, '%M %e, %Y %h:%i %p') as post_date from users join posts on users.id = posts.user_id order by posts.id DESC"
    posts = mysql.query_db(posts_query)

    # query comments and store in []
    comments_query = "SELECT users.id as commenter_id, users.first_name as commenter_name, comments.comment,  comments.post_id, DATE_FORMAT(comments.created_at, '%M %e, %Y %h:%i %p') as comment_date from users join comments on users.id = comments.user_id"
    comments = mysql.query_db(comments_query)
    return render_template('wall.html', posts=posts, comments=comments)


@app.route('/posts', methods=['POST'])
def post():
    if 'u_id' not in session:
        return redirect('/')
    #grab post text from wall form and insert into db redirect to wall
    post = request.form['post']
    if len(post) < 1:
        return redirect('/wall')
    query = 'INSERT INTO posts (user_id, content, created_at, updated_at) VALUES (:u_id, :content, NOW(), NOW())'
    data = {
        'u_id' : session['u_id'],
        'content' : post
    }
    post_id = mysql.query_db(query, data)  #not sure if I will need the id returned from the insert but will grab incase 
    return redirect('/wall')


@app.route('/comment', methods=['POST'])
def comment():
    if 'u_id' not in session:
        return redirect('/')
    # grab comment text and post id and insert into db - redirect to wall
    comment = request.form['comment']
    if len(comment) < 1:
        return redirect('/wall')
    post_id = request.form['post_id']
    query = "INSERT INTO comments (user_id, post_id, comment, created_at, updated_at) VALUES (:u_id, :post_id, :comment, NOW(), NOW())"
    data = {
        'u_id' : session['u_id'],
        'post_id' : post_id,
        'comment' : comment
    }
    comment_id = mysql.query_db(query, data)
    return redirect('/wall')



@app.route('/delete', methods=['POST'])
def delete():
    if 'u_id' not in session:
        return redirect('/')
    #add delet button to comments - if delete button pushed - check u_id against post id -allow delete if match delete from db - redirect to wall
    return redirect('/wall')


@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")


app.run(debug=True)