from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 
from time import gmtime, strftime, localtime

def index(request):
    return render(request, 'amadon_store/index.html')


def buy(request):
    #initalize session vars
    if 'grand_total' not in request.session:
        request.session['grand_total'] = 0
    if 'order_total' not in request.session:
        request.session['order_total'] = 0
    if  'total_number_orders' not in  request.session:
         request.session['total_number_orders'] = 0

    producct_id =request.POST['product_id']
    product_guide = {
        '1020' : {'item': 'Acoustic Guitar', 
                'price' : 4995},
        '1005' : {'item': 'Electric Guitar', 
                'price' : 2650},
        '1074' : {'item': 'Bass', 
                'price' : 2900}      
        }

    current_purchace = {
        'quantity' : request.POST['quantity'],
        'item' : product_guide[producct_id]['item'],
        'price' : product_guide[producct_id]['price']
        }

    request.session['item'] =  product_guide[producct_id]['item']
    order_total = int(current_purchace['quantity']) * current_purchace['price']
    request.session['order_total'] = order_total
    request.session['grand_total'] += order_total
    request.session['total_number_orders'] += 1

   

    return redirect('/amadon/checkout')


def checkout(request):
    return render(request, 'amadon_store/checkout.html', request.session)