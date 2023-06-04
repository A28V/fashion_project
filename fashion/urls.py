"""fashion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from users import views
from contact_details import views as contact
from catalog_settings import views as catalog
from cart import views as cart
from blog import views as blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',views.reg,name='reg'),
    path('reg/user',views.regUser,name="reg-user"),
    path('login',views.login,name="login"),
    path('login/user',views.loginUser,name="login-user"),
    path('home',views.home,name="home"),
    path('',views.home),
    path('contact',contact.contact,name="contact"),
    path('contact-user',contact.contactUser,name="contact-user"),
    path('logout',views.logout,name="logout"),
    path('about-us',views.aboutus,name="aboutus"),
    path('faq',views.faq,name="faq"),
    path('blog',blog.blogs,name="blog"),
    path('blog/<slug:url>', blog.blog,name='blog-view'),
    path('comment', blog.comments,name='blog-comments'),
    path('product/<slug:url>',catalog.product_details,name="catalog"),
    path('catalog/<slug:url>',catalog.category_details,name="catalog"),
    path('catalog/product/<int:id>',catalog.product_details,name="product"),
    path('shopping/',catalog.shopping,name="shop"),
    path('cart/add/<int:product_id>', cart.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>', cart.cart_remove, name='cart_remove'),
    path('cart/', cart.cart_detail, name='cart_detail'),
    path('orders/', include('order.urls')),
    path('accessories',views.accessories,name="accessories"),
    path('team',views.team,name="team"),
    path('terms',views.terms,name="terms"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
