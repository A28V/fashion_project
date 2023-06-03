from django.urls import path
from . import views

urlpatterns = [
    path(r'<str:url>', views.blog, name='blog_create'),
]
