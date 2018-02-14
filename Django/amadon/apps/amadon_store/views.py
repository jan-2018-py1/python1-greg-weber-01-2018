from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 
from time import gmtime, strftime, localtime

def index(request):
    return render(request, 'amadon_store/index.html')


def buy(request):
    #handel buying logic
    return redirect('amadon/buy')

def checkout(request):
    return render(request, 'checkout.html')