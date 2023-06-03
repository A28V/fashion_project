from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse;
from contact_details.models import ContactDetails
# Create your views here.
def contact(request):
	title= {"title":"Contact us"}
	return render(request,'contact.html',title)

@csrf_exempt
def contactUser(request):
	for key,value in request.POST.items():
		if request.POST.get(key) == "":
			return render(request,"contact.html",{'error':True})
	name=request.POST.get('name')
	email=request.POST.get('email')
	subject=request.POST.get('subject')
	contact_number=request.POST.get('phone')
	message=request.POST.get('message')
	datauser = ContactDetails(name=name,email=email,subject=subject,contact_number=contact_number,message=message)
	datauser.save()
	return HttpResponse("Thank you for letting us know! If you have any other questions or concerns, feel free to ask.")