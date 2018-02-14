from django.shortcuts import render, redirect, HttpResponse

def index(req):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(req):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(req):
    return redirect('/blogs')

def show(req, number):
    response = 'placeholder to display blog {}'.format(number)
    return HttpResponse(response)


def edit(req, number):
    response = 'placeholder to edit blog {}'.format(number)
    return HttpResponse(response)

def distroy(req, number):
    return redirect('/blogs')