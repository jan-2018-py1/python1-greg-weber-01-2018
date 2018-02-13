from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 


def index(request):
    return render(request, 'session_words/index.html')


def add(request):
   # use a list to hold dicts of data for each submit
    if 'data' not in request.session:
        request.session['data'] = []
    new_word_data = {
        'word' :  request.POST['word'],
        'color' : request.POST['color'],
    }
    #setting a var state for fontsize from the checkbox field
    if 'big_font' not in request.POST:
        new_word_data['big_font'] = 'off'
    else:
        new_word_data['big_font'] = 'on'
    #append new data
    request.session['data'].append(new_word_data)
    #print request.session['data']
    for data in request.session['data']:
        print data['word'], data['color']
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')