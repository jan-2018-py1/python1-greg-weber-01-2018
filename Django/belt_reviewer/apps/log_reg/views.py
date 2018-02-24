from django.shortcuts import render, HttpResponse, redirect
from models import *

from django.contrib import messages

def index(req):
    #render the index page with log/reg forms
    if 'user_id' not in req.session:
        req.session['user_id'] = ''
    return render(req, 'log_reg/index.html')

def show(req):
    # show user name and sucess message use session user_id
    return render(req, 'log_reg/success.html', req.session)

def create(req):
    # validate/create user, login user into session and redirect to show upon success or redirect with errors 
    errors = User.objects.reg_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')        
    else:
        # grab post data and insert into db
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        password = User.objects.password_hasher(req.POST['password']) #hashes pwd in models
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        #login to sessions
        req.session['user_id'] = new_user.id
        return redirect('/success')

def login(req):
    # use login_validator method to check if info matches in db, then redirect to show or error messages to index
    
    errors = User.objects.login_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')    
    else: #log user into session
        this_user = User.objects.get(email=req.POST['email'])
        req.session['user_id'] = this_user.id
        return redirect('/success')
        
def logout(req):
    req.session.clear()
    return redirect('/')