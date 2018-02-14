from django.shortcuts import render, redirect, HttpResponse


def index(req):
    response = 'placeholder to display all the surveys created'
    return HttpResponse(response)

def new(req):
    response = 'placeholder for users to add a new survey'
    return HttpResponse(response)