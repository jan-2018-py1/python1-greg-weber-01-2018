from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this_time_its_payback'
import random 
from time import ctime

# note: I didn't use the session['mood'] key that I set up, I wanted to figuire out how to log all the activity in 
# order regardless of getting gold or loseing gold, but since they need to have different text color I haven't 
# fuigured how to do that yet. I made a different key in sessions for each activity - get gold or loose gold - and 
# then logged that in my html one after the other.  My thought to log all regardless of color would be to store 
# info in a list or dict and then append that to session['activity'] - so all info in one key of session rather
#  than two ... so it would end up looking like [{'happy':'got gold'},{'sad':'lost gold'}, ....] -- then use some 
# conditionals and loops to extract the correct info and display the correct text color.  
 
@app.route('/')
def home():
    #initalize gold vars if they haven't been used yet
    if 'gold_count' not in session:
        session['gold_count'] = 0
        session['farm_gold'] = 0
        session['cave_gold'] = 0
        session['house_gold'] = 0
        session['casino_gold'] = 0
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
        session['farm_gold'] = random.randrange(10, 21)
        session['gold_count'] += session['farm_gold']
        string = 'Earned {} gold from the farm! ({})'.format(session['farm_gold'], now)
        session['got_gold'].append(string)
        # session['mood'] = 'happy'

    if request.form['building'] == 'cave':
        session['cave_gold'] = random.randrange(5, 11)
        session['gold_count'] += session['cave_gold']
        string = 'Earned {} gold from the cave! ({})'.format(session['cave_gold'], now)
        session['got_gold'].append(string)
        # session['mood'] = 'happy'

    if request.form['building'] == 'house':
        session['house_gold'] = random.randrange(2,6)
        session['gold_count'] += session['house_gold']
        string = 'Earned {} gold from the house! ({})'.format(session['house_gold'], now)
        session['got_gold'].append(string)
        # session['mood'] = 'happy'

    #random 0 or 1 will give 50/50 give/take value to casino gold
    give_take = random.randrange(0,2)
    if request.form['building'] == 'casino':
        session['casino_gold'] = random.randrange(0, 51)
        if give_take == 0:
            session['gold_count'] += session['casino_gold']
            string = 'Winner!! You won {} gold at the casino! ({})'.format(session['casino_gold'], now)
            session['got_gold'].append(string)
            # session['mood'] = 'happy'
        else:
            session['gold_count'] -= session['casino_gold']
            string = 'Ahhhh, too bad... you lost {} gold from the casino! ({})'.format(session['casino_gold'], now)
            session['lost_gold'].append(string)
            # session['mood'] = 'sad'

    return redirect('/')

app.run(debug=True)