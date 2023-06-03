from django.shortcuts import render
from django.http import HttpResponseRedirect;
from blog.models import *
# Create your views here.
from django.contrib import messages

def blog(request,url):
	blog = Blog.objects.filter(key=url).values()
	topthreeblog = Blog.objects.all().order_by('id')[:3]
	blog_id = blog[0]['id']
	blog_comment = BlogCommentadd.objects.filter(blog_id=blog_id).values()
	return render(request,'blogs.html',{'title':'Blogs','blog':blog,'url':url,'blog_comment':blog_comment,'topthreeblog':topthreeblog})



def comments(request):
	if request.method=="POST":
   	    name = request.POST.get("name")
   	    email = request.POST.get("email")
   	    comment = request.POST.get("comment")
   	    urlkey = request.POST.get('urlkey')
   	    blog_id = request.POST.get('blog_id')
   	    comment = BlogCommentadd(name=name,email=email,comment=comment,blog_id=blog_id)
   	    comment.save()
   	    messages.success(request, 'Thanks for Your Feedback! '+name)
   	    return HttpResponseRedirect("/blog/"+urlkey)
	

def blogs(request):
	allblog = Blog.objects.all()
	data = {'title':'blog','allblog':allblog}
	return render(request, 'blog_page.html',data)