from django.shortcuts import render, HttpResponse

def index(req):
    return HttpResponse('Hey you, world')
