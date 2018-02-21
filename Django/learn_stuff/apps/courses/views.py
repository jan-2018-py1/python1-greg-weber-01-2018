from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages


def index(req):   
    context = {
        'courses' : Course.objects.all()
    }
    return render(req, 'courses/index.html', context)

def new(req):
    errors = Course.objects.validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        course = Course.objects.create(name=req.POST['name'])
        description = Description(summary=req.POST['description'], course=course)
        description.save()
    return redirect('/')

def edit(req, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def destroy(req, id):
    context = {
        'course' : Course.objects.get(id=id)
    }
    return render(req, 'courses/destroy.html', context)