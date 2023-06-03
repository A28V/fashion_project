from django.db import models

# Create your models here.

from django.db import models
from tinymce.models import HTMLField
class Blog(models.Model):
	name=models.CharField(max_length=200)
	key =models.SlugField(default="", null=False,unique=True,help_text="Please enter a valid url key")
	pic=models.ImageField(upload_to='blog/')
	short_description = models.TextField(blank=True,null = True)
	content = HTMLField(blank=True,null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class BlogComment(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	comment = models.TextField(blank=True,null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class BlogCommentadd(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	comment = models.TextField(blank=True,null = True)
	blog_id = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)