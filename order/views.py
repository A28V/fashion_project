from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from order.models import pay_status
from django.http import HttpResponseRedirect;
import json
def order_create(request):
    cart = Cart(request)
    if not request.session['cart']:
        return HttpResponseRedirect('/home') 
    if request.method == 'POST':
        pay_method = request.POST.get('pay_method')
        form = OrderCreateForm(request.POST)
        order = ''
            #cart.clear()
        if pay_method == 'cash_on':
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )


            cart.clear()
            
            request.session['orderid']=order.id
            return HttpResponseRedirect('/orders/order-success')
        else:
            if request.session['userid']:
                addressInjson = json.dumps(request.POST)
                return render(request, 'orders/order/pay.html', {'cart':cart,'useraddress':addressInjson})
            else:
                return HttpResponseRedirect('/login')
    else:
        form = OrderCreateForm()
        cart = Cart(request)
        if 'userid' in request.session:
            return render(request, 'orders/order/create.html', {'form': form,'cart':cart})
        else:
            request.session['url_key']='/orders/create'
            return HttpResponseRedirect('/login')


def pay(request):
    cart = Cart(request)
    if request.method == 'POST':
        user_id=request.session['userid']
        email = request.POST.get('email')
        oid = request.POST.get('oid')
        amout = request.POST.get('amount')
        pay = pay_status(userId=user_id,email=email,ORDERID=oid,amount=amout)
        pay.save()
        cart= Cart(request)
        cart.clear()
        return render(request,'orders/order/created.html',{'title':'Order Success','orderid':oid})

def pay(request):
    # Process the payment response from Paytm
    # Retrieve the response parameters
    response_dict = dict(request.POST)
    response_dict.pop('csrfmiddlewaretoken', None)
   
    # Verify the response integrity with the checksum
    paytm_checksum = response_dict.pop('CHECKSUMHASH')[0]
    is_valid_checksum = verify_checksum(response_dict, paytm_checksum)
    

    if is_valid_checksum:
        # Payment is successful, process the order
        # You can access the response parameters like response_dict['ORDERID'][0], response_dict['TXNAMOUNT'][0], etc.
        # Process the order and update your database accordingly
        request.session['orderid']=order.id
        return HttpResponseRedirect('/orders/order-success')
        return render(request, 'payment_success.html', {'response_dict': response_dict})
    else:
        # Payment is unsuccessful
        return render(request, 'payment_failure.html')

def generate_checksum(payload):
    paytm_params = dict(payload)
    checksum = PaytmChecksum.generateSignature(paytm_params, 'YOUR_MERCHANT_KEY')
    return checksum

def verify_checksum(payload, checksum):
    paytm_params = dict(payload)
    is_valid_checksum = PaytmChecksum.verifySignature(paytm_params, 'YOUR_MERCHANT_KEY', checksum)
    return is_valid_checksum


def order_success(request):
    return render(request,'orders/order/created.html',{'title':'Order Success','orderid':request.session['orderid']})