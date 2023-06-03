from django.urls import path
from . import views

urlpatterns = [
    path(r'create/', views.order_create, name='order_create'),
    path('pay/', views.pay, name='pay'),
    path('order-success/', views.order_success, name='order-success'),

]
