from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = 0
    session['count'] +=1
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_button():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = -1
    return redirect('/')

app.run(debug=True)




