from django.urls import path
from catalog_settings import views as catalog

app_name = 'cart'

urlpatterns = [
    #path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', catalog.shopping, name='cart_add'),
    #path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
]

