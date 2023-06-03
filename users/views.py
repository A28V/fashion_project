from django.shortcuts import render
from users.models import UsersConfig
from django.http import HttpResponse;
from django.http import HttpResponseRedirect;
from django.contrib import messages
from catalog_settings.models import *
from cart.forms import CartAddProductForm
from blog.models import *
# from team.models import *

def reg(request):
	title= {"title":"Registration page"}
	return render(request,"registration.html",title)
# Create your views here.

def regUser(request):
    for key,value in request.POST.items():
    	if request.POST.get(key) == "":
    		return render(request,"registration.html",{'error':True})

    if request.method=="POST":
   	    email = request.POST.get("email")
   	    password = request.POST.get("password")
   	    confirm_password = request.POST.get('confirm_password')
   	    dataToregUser = UsersConfig.objects.filter(email=email).values()
   	    emailTouser = ""
   	    for data in dataToregUser:
   	    	emailTouser = data['email'];
   	    #emailToregUser = UsersConfig.objects.values_list('email', flat=True).distinct()
   	    if emailTouser=="":
   	        if password == confirm_password:
   	            datauser = UsersConfig(email=email,password=password)
   	            datauser.save()
   	            messages.success(request, 'Account created! Welcome to our platform.')
   	            return HttpResponseRedirect("/login")
   	        else:
   	            messages.success(request, 'Confirm your password to proceed, for security purposes.')
   	            return HttpResponseRedirect("/reg")
   	    else:
   	    	messages.success(request, 'Account exists. Please log in to access.')
   	    	return HttpResponseRedirect("/login")


def login(request):
	title= {"title":"Login page"}
	return render(request,"login.html",title)


def loginUser(request):
	if request.method=="POST":
		email = request.POST.get("email")
		dataToregUser = UsersConfig.objects.filter(email=email).values()
		emailTouser = ""
		for data in dataToregUser:
			emailTouser = data['email'];
		if emailTouser!="":
		    emaild = dataToregUser[0]['email']
		    password = request.POST.get("password")
		    passwordToregUser = dataToregUser[0]['password']
		    if password == passwordToregUser:
		        request.session['userid'] = dataToregUser[0]['id']
		        request.session['useremail'] = dataToregUser[0]['email']
		        if 'url_key' not in request.session:
		        	return HttpResponseRedirect('/home')
		        else:
		        	return HttpResponseRedirect(request.session['url_key'])
		    else:
			    messages.error(request, 'Password error. Please re-enter and try again.')
			    return HttpResponseRedirect('/login')
		else:
			messages.error(request, 'No account found. Please create a new one.')
			return HttpResponseRedirect('/login')



def logout(request):
	request.session['userid'] = 0
	request.session['useremail'] = ""
	return HttpResponseRedirect('/login') 

def home(request):
	categories = Category.objects.all()
	blog = Blog.objects.all().order_by('id')[:3]
	prd=products.objects.all()
	cart_product_form= CartAddProductForm()
	return render(request,"after_home.html",{"title":"Home page",'categories':categories,'prd':prd,'blog':blog})
	#return render(request,"after_home.html",{"title":"Home page"})

def accessories(request):
	#categories = Category.objects.all()
	# prd=products.objects.all()
	categories = Category.objects.values('id','name')
	cat_product = []
	for cat in categories:
		prd=products.objects.filter(catid=cat['id'])
		categories=Category.objects.filter(id=cat['id'])
		#prdd=products.objects.filter(catid=cat['id']).values()
		if prd.exists():
			cat_product.append([categories,prd])
	print(cat_product);
	cart_product_form= CartAddProductForm()
    #data={'prd':prd,'cart_product_form':cart_product_form}
    #data={'prd':prd,'cart_product_form':cart_product_form,'categories':categories}
	return render(request,"accessories.html",{'cat_product':cat_product,'title':'Accessories'})

	#return render(request, 'accessories.html',{"title":"Accessories page",'categories':categories,'prd':prd})

def jeans(request):
	title = {'title':'jeans page'}
	return render(request, 'jeans.html',title)

def shirts(request):
	title = {'title':'shirts page'}
	return render(request, 'shirts.html',title)

def aboutus(request):
	title = {'title':'About Us'}
	return render(request, 'about_us.html',title)


def faq(request):
	title = {'title':'FAQs'}
	return render(request, 'faq.html',title)

def blog(request):
	blog = Blog.objects.all().order_by('id')[:3]
	blogdata = {'title':'blog','blog':blog}
	return render(request, 'blogs.html',blogdata)

def terms(request):
	title = {'title':'terms'}
	return render(request, 'terms.html',title)

def team(request):
	title = {'title':'team'}
	return render(request, 'team.html',title)

def custom_404_error(request, exception):
    return render(request, '404.html', status=404)