from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 

def random_word(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1
    rando =  {'result' : get_random_string(length=14)}
    return render(request, 'random_word/random_word.html', rando)

    
def generate_new(request):
    return redirect('/random_word')

def reset_counter(request):
    request.session['attempt'] = 0
    return redirect('/random_word')