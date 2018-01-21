from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "vallllliiiid1at7ior"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    #setup error boolean
    error = False

    #validification checks
    if len(request.form['name']) < 1:
        flash("*** Name cannot be empty! ***")
        error = True
    if len(request.form['location']) < 1:
        flash("*** Location cannot be empty! ****")
        error = True
    if len(request.form['comment']) > 121:
        flash("*** comment cant be longer than 120 characters! ****")
        error = True

    #redirect if error or render results page if no error
    if error == True:
        return redirect('/')
    else:
        return render_template('/results.html', name = request.form['name'], location = request.form['location'],  language = request.form['language'], comment = request.form['comment'], )

@app.route('/return', methods=['POST'])
def go_home():
    return redirect('/')
app.run(debug=True)

