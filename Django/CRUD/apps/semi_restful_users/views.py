from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    return render(req, 'semi_restful_users/index.html')


def new(req):

    return render(req, 'semi_restful_users/new.html')

def edit(req, id):

    return render(req, 'semi_restful_users/edit.html')

def show(req, id):

    return render(req, 'semi_restful_users/new.html')

def create(req):

    return redirect('/users/<id>')

def destroy(req, id):
    return redirect('/users')

def update(req, id):
    return redirect(req, 'semi_restful_users/users/<id>')




