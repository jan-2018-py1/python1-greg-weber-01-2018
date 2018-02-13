from django.shortcuts import render, redirect


def index(request):
    return render(request,'surveys/index.html')


def process(request):
    if 'submit_counter' not in request.session:
        request.session['submit_counter'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment']  = request.POST['comment']
    request.session['submit_counter'] += 1 #counts number of times form had been submitted
    return redirect('/result')


def result(request):
    return render(request, 'surveys/results.html')