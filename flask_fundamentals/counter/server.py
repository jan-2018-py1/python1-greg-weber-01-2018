from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def view_count():
    session['count'] +=1
    return redirect('/')
app.run(debug=True)


