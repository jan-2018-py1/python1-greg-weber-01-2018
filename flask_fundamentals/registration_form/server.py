from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "a;sklj;lkjdfa"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # set boolean for blank field
    blank_field = True

    #check first name for not blank and no numbers
    

    #check last name for not blank and no numbers

    #check email for not blank and valid format


    #check password for not blank and <= 8 characters

    #check password confirm for not blank and match password

    if blank_field:
        print 'error message about blank field'


    return redirect('/')
app.run(debug=True)