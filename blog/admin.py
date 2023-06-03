from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display= ['name','created_at','updated_at']

    

class blogCommitDetailsAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','comment','blog_id','created_at','updated_at']
admin.site.register(BlogCommentadd,blogCommitDetailsAdmin)



admin.site.register(Blog,BlogAdmin)

