from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'The_secret'
import random

@app.route('/')
def home():
    if 'random_num' not in session:
        session['random_num'] = random.randrange(0,101)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return render_template('game.html')

@app.route('/reset', methods=['POST'])
def reset():
    session['random_num'] = random.randrange(0,101)
    return redirect('/')

app.run(debug=True)
