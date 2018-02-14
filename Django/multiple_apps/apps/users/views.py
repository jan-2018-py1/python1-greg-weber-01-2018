from django.shortcuts import render, redirect, HttpResponse


def register(req):
    response = 'placeholder for users to create a new user record'
    return HttpResponse(response)

def login(req):
    response = 'placeholder for users to login'
    return HttpResponse(response)

def users(req):
    response = 'placeholder to later display all the list of users'
    return HttpResponse(response)