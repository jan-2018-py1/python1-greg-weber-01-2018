from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(req):
    users = User.objects.all()
    print 'users:', users
    context = {
        'users': users
    }
    return render(req, 'semi_restful_users/index.html', context)

def new(req):
    return render(req, 'semi_restful_users/new.html')

def edit(req, id):
    if 'user_id' not in req.session:
        req.session['user_id'] = id
    user = User.objects.get(id=id)
    context = {
        'this_user': user
    }
    return render(req, 'semi_restful_users/edit.html', context)

def show(req, id):
    user = User.objects.get(id=id)
    context = {
        'this_user': user
    }
    return render(req, 'semi_restful_users/show.html', context)

def create(req):
    User.objects.create(name=req.POST['name'], email=req.POST['email'])
    new_user = User.objects.last() 
    user_id = new_user.id
    url = '/users/{}'.format(user_id)
    return redirect(url)

def destroy(req, id):
    this_user = User.objects.get(id=id)
    this_user.delete()
    return redirect('/users')

def update(req):
    user = User.objects.get(id=req.session['user_id'])
    user.name = req.POST['name']  
    user.email = req.POST['email']
    user.save()
    user_id = req.session['user_id']
    url = '/users/{}'.format(user_id)
    return redirect(url)




