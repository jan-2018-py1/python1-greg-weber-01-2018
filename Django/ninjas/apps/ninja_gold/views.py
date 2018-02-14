from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 
from time import gmtime, strftime, localtime
import random 
from time import ctime


def index(request):
    #initalize sessions if they haven't been used yet
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
        request.session['activity'] = []
    return render(request,'ninja_gold/index.html')

def process_money(request):
    #empty string to build activity log
    action = '' 
    #empty list to build activity log, the first index will hold a string with either green or red that will be used in the html template as a class atribute so that the event action will be styled the correct color.
    event = []
    #determine date/time 
    now = ctime()

    if request.POST['building'] == 'farm':
        gold = random.randrange(10, 21)
        request.session['gold_count'] += gold
        action = 'Earned {} gold from the farm! ({})'.format(gold, now)
        event = ['green', action]
        request.session['activity'].insert(0, event)

    if request.POST['building'] == 'cave':
        gold = random.randrange(5, 11)
        request.session['gold_count'] += gold
        action = 'Earned {} gold from the cave! ({})'.format(gold, now)
        event = ['green', action]
        request.session['activity'].insert(0, event)

    if request.POST['building'] == 'house':
        gold = random.randrange(2,6)
        request.session['gold_count'] += gold
        action = 'Earned {} gold from the house! ({})'.format(gold, now)
        event = ['green', action]
        request.session['activity'].insert(0, event)

    if request.POST['building'] == 'casino':
        gold = random.randrange(-50, 51)
        if gold > -1:
            request.session['gold_count'] += gold
            action = 'Winner!! You won {} gold at the casino! ({})'.format(gold, now)
            event = ['green', action]
            request.session['activity'].insert(0, event)
        else:
            request.session['gold_count'] -= gold
            action = 'Ahhhh, too bad... you lost {} gold from the casino! ({})'.format(gold, now)
            event = ['red', action]
            request.session['activity'].insert(0, event) 
    print '++'*50
    print request.session['activity']   
    return redirect('/')

def reset():
    request.session['gold_count'] = 0
    request.session['activity'] = []
    return redirect('/')


