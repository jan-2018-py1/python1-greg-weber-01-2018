from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 


def index(request):
    return render(request, 'session_words/index.html')


def add(request):
    #use a list to hold dicts of data for each submit
    if 'data' not in request.session:
        request.session['data'] = []
    #setting a var for fontsize from the checkbox field
    
    print request.POST['big_font']
   
    new_word_data = {
        'word' :  request.POST['word'],
        'color' : request.POST['color'],
        'big_font' : request.POST['big_font']
    }
    #append new data
    request.session['data'].append(new_word_data)
    print request.session['data']
    return redirect('/session_words')

def clear(request):
    # request.session.clear()
    return redirect('/session_words')