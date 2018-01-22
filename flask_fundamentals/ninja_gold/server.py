from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this_time_its_payback'
import random 
from time import ctime
 
@app.route('/')
def home():
    #initalize sessions if they haven't been used yet
    if 'gold_count' not in session:
        session['gold_count'] = 0
        session['activity'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def gold_digger():
    #empty string to build activity log
    string = '' 
    #empty list to build our activity log
    event = []
    #determine date/time 
    now = ctime()

    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        session['gold_count'] += gold
        string = 'Earned {} gold from the farm! ({})'.format(gold, now)
        event = ['green', string]
        session['activity'].insert(0, event)

    if request.form['building'] == 'cave':
        gold = random.randrange(5, 11)
        session['gold_count'] += gold
        string = 'Earned {} gold from the cave! ({})'.format(gold, now)
        event = ['green', string]
        session['activity'].insert(0, event)

    if request.form['building'] == 'house':
        gold = random.randrange(2,6)
        session['gold_count'] += gold
        string = 'Earned {} gold from the house! ({})'.format(gold, now)
        event = ['green', string]
        session['activity'].insert(0, event)

    if request.form['building'] == 'casino':
        gold = random.randrange(-50, 51)
        if gold > -1:
            session['gold_count'] += gold
            string = 'Winner!! You won {} gold at the casino! ({})'.format(gold, now)
            event = ['green', string]
            session['activity'].insert(0, event)
        else:
            session['gold_count'] -= gold
            string = 'Ahhhh, too bad... you lost {} gold from the casino! ({})'.format(gold, now)
            event = ['red', string]
            session['activity'].insert(0, event)
           
    return redirect('/')

@app.route('/reset')
def reset():
    session['gold_count'] = 0
    session['activity'] = []
    return redirect('/')

app.run(debug=True)