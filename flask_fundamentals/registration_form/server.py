from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "a;sklj;lkjdfa"
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # set booleans
    blank_field = False
    name_has_num = False
    password_match = True
    password_too_long = False
    email_valid = True
    
    #check for blank field
    if len(request.form['f_name']) < 1:
        blank_field = True
    if len(request.form['l_name']) < 1:
        blank_field = True
    if len(request.form['email']) < 1:
        blank_field = True
    if len(request.form['password']) < 1:
        blank_field = True
    if len(request.form['re_password']) < 1:
        blank_field = True

    #function to check a string for numbers. I know this is probably overkill because I only use it once but it was fun to write. 
    #thanks to help from TA nick for making it more elegant and pythonic...
    def check_for_num(my_string):
        for character in range(len(my_string)):
            if my_string[character].isdigit():
                return True 
            
    #check name for any characters that might be a number using above finction - sets name_has_num to True if number found
    full_name = request.form['f_name'] + request.form['l_name']
    name_has_num = check_for_num(full_name)

    #check for password match
    password_match = request.form['password'] == request.form['re_password']

    #check for passwoprd too long
    if len(request.form['password']) > 8:
        password_too_long = True

    #check validity of email
    email_valid = EMAIL_REGEX.match(request.form['email'])


    #flash message errors
    if blank_field:
        flash("*** All fields are required and must not be blank ***")
    if name_has_num:
        flash("*** Names must not contain any numbers ***")
    if password_too_long:
        flash("*** Pasword too long - must be 8 or fewer characters ***")
    if not password_match:
        flash("*** Passwords must match! ***")
    if not email_valid:
        flash('*** Invalid email address ***')


    #flash message for successful registration
    if not blank_field and not name_has_num and password_match and not password_too_long and email_valid:
        flash(" <---Thanks for submitting your information--->")

    return redirect('/')
app.run(debug=True)