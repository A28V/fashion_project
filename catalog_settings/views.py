from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator

def category_details(request, url):
	cart_product_form= CartAddProductForm()
	product = get_object_or_404(Category, url=url)
	category = Category.objects.filter(url=url)
	categoryname = Category.objects.filter(url=url).values('name')
	categories = Category.objects.all()
	prd=products.objects.filter(catid=category[0])
	paginator = Paginator(prd, 4)  # Show 25 contacts per page.
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)
	data={'title':categoryname[0]['name'],'prd':page_obj,'cart_product_form':cart_product_form,'categories':categories}
	return render(request,"shopping.html",data)

def product_details(request, url):
	cart_product_form= CartAddProductForm()
	# product = get_object_or_404(Category, url=url)

	# categories = Category.objects.all()
	prd=products.objects.filter(id=url).values()
	catid_id=''
	product_id = ''
	productname = ''
	for data in prd:
			catid_id = data['catid_id'];
			product_id = data['id']
			productname = data['name']
	product = products.objects.filter(catid_id=catid_id).exclude(id=product_id)

	return render(request,"catalog_product_view.html",{'title':productname,'prd':prd,'cart_product_form':cart_product_form,'product':product,'product_id':url})


def shopping(request):
    prd=products.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(prd, 4)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    cart_product_form= CartAddProductForm()
    #data={'prd':prd,'cart_product_form':cart_product_form}
    data={'title':'Product List','prd':page_obj,'cart_product_form':cart_product_form,'categories':categories}
    return render(request,"shopping.html",data)



