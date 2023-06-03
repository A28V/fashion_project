from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from catalog_settings.views import products
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import json
from decimal import Decimal
# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    product = get_object_or_404(products, id=product_id) 
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(products, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # decimal_value=Decimal(str(len(cart)))
    # json_str = json.dumps({'income': decimal_value})
    # request.session['aaa'] = 'okk'
    # print(decimal_value)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart.html', {'cart': cart,'title':'Check Out'})

