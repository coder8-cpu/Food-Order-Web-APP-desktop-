"""bress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import Settings
from django.contrib import admin
from django.urls import path
from login import views
from login.views import *
from django.conf import settings
from django.conf.urls.static import static
main = main()
obj1 = navs()
obj2 = navs()
obj3 = navs()
obj4 = navs()
obj5 = navs()
obj6 = navs()
obj7 = navs()
obj8 = navs()
obj9 = navs()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",main.index),
    path('index/<nav>/',obj1.navbar),
    path('dishes/<nav>/',obj2.navbar),
    path('about/<nav>/',obj3.navbar),
    path('services/<nav>/',obj4.navbar),
    path('order/<nav>/',obj5.navbar),
    path('search/<nav>/',obj6.navbar),
 
    
    path('menu/<nav>/',obj9.navbar),



    path("",main.signup),
    
    path("dishes/",main.dishes),
    path("order/",main.order),
    path("about/",main.about),
    path("menu/",main.menu),
    path("search/",main.searchh),
    path("signup/",main.signup),
    path("login/",main.login),
    path("index/payment",main.pay),
    path("www.facebook.com/",main.face_book),
    path("www.instagram.com/",main.insta_gram),
    path("www.twitter.com/",main.twi_tter),
    path("www.behance.com/",main.beha_nce),
    path("payment",main.pay),
    path("dishes/<foodcode>/profile/cart",main.cart),
    path("<foodcode>/profile/cart",main.cart),
    path("profile/",main.profile),
    path("index/<foodcode>/profile/cart/",main.cart),
    path("menu/<foodcode>profile/cart/",main.cart),
 
    path("logout/",main.logout),
    path("dishes/profile/cart/",main.show_cart),
    path("profile/orderhistory/",main.order_hist),
    path("thankyou",main.thanks),
    path("dishes/profile/cart/<foodcode>/",main.cart),
    path("cart/",main.cart)]
    

    
   

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
