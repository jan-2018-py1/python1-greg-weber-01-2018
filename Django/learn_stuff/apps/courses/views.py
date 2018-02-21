from django.shortcuts import render, HttpResponse, redirect

def index(req):

    return render(req, 'courses/index.html')

def destroy(req, id):
    return render(req, 'courses/destroy.html')