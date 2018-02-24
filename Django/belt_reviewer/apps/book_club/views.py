from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(req):
    return HttpResponse('got here')
