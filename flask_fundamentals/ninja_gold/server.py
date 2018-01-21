from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this_time_its_payback'
import random 
from time import ctime

# note: I didn't use the session['mood'] key that I set up, I wanted to figuire out how to log all the activity in 
# order regardless of getting gold or loseing gold, but since they need to have different text color I haven't 
# fuigured how to do that yet. I made a different key in sessions for each activity - get gold or loose gold - and 
# then logged that in my html one after the other.  My thought to log all regardless of color would be to store 
# info in a list or dict and then append that to session['activity'] - so all info in one key of session rather  than two ... 
# so it would end up looking like activity['session'] = [{'color':'green', 'event':'got gold...'},{'color':'red', 'event: lost gold'}, ...]
# then use the color value to set the class in the html and the activity value to log the activity  
 
@app.route('/')
def home():
    #initalize gold vars if they haven't been used yet
    if 'gold_count' not in session:
        session['gold_count'] = 0
        session['got_gold'] = [] #a liist to store the activity log when we get gold
        session['lost_gold'] = [] #a liist to store the activity log when we loose gold
        #session['mood'] = '' #this will help us determine which activity to print
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def gold_digger():

    string = '' #we will use this string to build our activity log

    #determine date/time 
    now = ctime()

    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        session['gold_count'] += gold
        string = 'Earned {} gold from the farm! ({})'.format(gold, now)
        session['got_gold'].append(string)
        session['mood'] = 'green'

    if request.form['building'] == 'cave':
        gold = random.randrange(5, 11)
        session['gold_count'] += gold
        string = 'Earned {} gold from the cave! ({})'.format(gold, now)
        session['got_gold'].append(string)
        session['mood'] = 'green'

    if request.form['building'] == 'house':
        gold = random.randrange(2,6)
        session['gold_count'] += gold
        string = 'Earned {} gold from the house! ({})'.format(gold, now)
        session['got_gold'].append(string)
        session['mood'] = 'green'

    if request.form['building'] == 'casino':
        gold = random.randrange(-50, 51)
        if gold > -1:
            session['gold_count'] += gold
            string = 'Winner!! You won {} gold at the casino! ({})'.format(gold, now)
            session['got_gold'].append(string)
            session['mood'] = 'green'
        else:
            session['gold_count'] -= gold
            string = 'Ahhhh, too bad... you lost {} gold from the casino! ({})'.format(gold, now)
            session['lost_gold'].append(string)
            session['mood'] = 'red'

    return redirect('/')

app.run(debug=True)