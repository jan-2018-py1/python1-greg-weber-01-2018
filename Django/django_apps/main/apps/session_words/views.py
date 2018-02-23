from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 
from time import gmtime, strftime, localtime

def index(request):
   # print request.session['data']
    return render(request, 'session_words/index.html')


def add(request):
   # use a list to hold dicts of data for each submit
    request.session['count'] = 0
    if 'data' not in request.session:
        request.session['data'] = []
    new_word_data = {
        'word' :  request.POST['word'],
        'color' : request.POST['color'],
        "time": strftime("%b %d, %Y %I:%M %p")
    }
    #set a var for font size from the checkbox field
    # try:
    #     request.post["big_font"]
    #     new_word_data["big_font"] = "on"
    # except:
    #     pass
    if 'big_font' not in request.POST:
        pass
    else:
        new_word_data['big_font'] = 'on'
    # new_word_data = 'big_font' not in request.POST ? "off" : "on"
    #append new data
    request.session['data'].append(new_word_data)
    request.session['count'] = 1 +  request.session['count']
    print request.session['count']

    print request.session['data']
    # for data in request.session['data']:
    #     print data['word'], data['color']
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')