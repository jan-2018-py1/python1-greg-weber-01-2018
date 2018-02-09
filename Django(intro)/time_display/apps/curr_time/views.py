from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
  context = {
  "time": strftime("%b %d, %Y %I:%M %p", localtime())
  }
  return render(request,'curr_time/index.html', context)