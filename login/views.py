from logging import LogRecord
from pickle import TRUE
import re
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
import login
from login.models import Dishes,Menu,Order,Searchhhh,specialdish,Review,Cart,Signup,Login,Active
from login import models
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


class main:
       
        def login(self,request):

            
                if request.user.is_authenticated:
                        return redirect("/index")
            
                if request.method == 'POST':
                    username = request.POST.get('name')
                    password = request.POST.get('pwd')

                    user = auth.authenticate(username = username, password = password)
                    
                    if user is not None:
                        auth.login(request,user)
                       
                        request.session['name'] = username
                                                
                       
                                    
                        return redirect("/index")
               
                
                        
                return render(request,"login.html",{"year":2022})
                
       
        def index(self,request):
           
            if request.user.is_authenticated:
                
                if request.method == 'POST':
                        revv = Review()
                        revv.name = request.POST.get('name')
                        revv.rev = request.POST.get('msg')

                        revv.save()
                        return redirect("/thankyou")
                        
                else:    
                    sd = specialdish.objects.all()
                        
                    d = Dishes.objects.all()[4:7]
                    m = Menu.objects.all()
                    r = Review.objects.all()
                    
                        
                        
                    
                        
                    
                    v = {"obj":sd,"objec":d,"oob":m,"oop":r,"year":2022,}

                    return render(request,"index.html",v)
            return HttpResponse("<h1> NET Error...  NOT allowed...... </h1>")
            
             
        
        
        def dishes(self,request):
            if request.user.is_authenticated:
            
                d = Dishes.objects.all()
                d = {"d":d,"year":2022}
               
                
                return render(request,"dishes.html",d,)
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def menu(self,request):
            if request.user.is_authenticated:
                m = Menu.objects.all()
                obj = {"obj":m,"year":2022}
                
            
                return render(request,"menu.html",obj)
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def order(self,request):
            if request.user.is_authenticated:
                if request.method == 'POST':
                
                    o = Order()
                    o.name = request.POST.get('name')
                    o.mobileno = request.POST.get('number')
                    o.code = request.POST.get('code')
                    o.food_name = request.POST.get('foodname')
                    o.extra_food = request.POST.get('extrafood')
                    o.count = request.POST.get('count')
                    o.address = request.POST.get('address')
                    o.msg = request.POST.get('msg')
                    o.save()

                    return redirect("/payment.html")
               

                year = {"year":2022}
                return render(request,"order.html",year)
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")
            
        def pay(self,request):
            if request.user.is_authenticated:
                return render(request, "payment.html")
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def review(self,request):
            if request.user.is_authenticated:
                if request.method == 'POST':
                    revv = Review()
                    revv.name = request.POST.get('name')
                    revv.rev = request.POST.get('msg')

                    revv.save()
                    return redirect("/popup")
                r = Review.objects.all()
                obj = {"obj":r,"year":2022}
                year = {"year":2022}
                

                
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def verify(self,request):
            if request.user.is_authenticated:
                return render(request,"verification.html")
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def search(self,request):
            if User.is_authenticated:
                
            
                return render(request,"search.html")

            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")
            
        def about(self,request):
            if request.user.is_authenticated:
                

                return render(request,"about.html",{"year":2022})
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def signup(self,request):
            
                
                if request.user.is_authenticated:
                    return redirect("/index")
                
                if request.method == 'POST':
                    ss = Signup.objects.all()
                    for i in ss:
                        if i.name == request.POST.get('name'):
                            messages.info(request,"UserName Taken")
                        
                            return redirect("/signup")
                    name = request.POST.get('name')
                    pwd = request.POST.get('pwd')
                    user = User.objects.create(username=name)
                    user.set_password(pwd)
                    
                    user.save()
                    s = Signup()
                    s.name = request.POST.get('name')
                    s.password = request.POST.get('pwd')
                    s.c_pwd = request.POST.get('pwd')
                    s.save()
                    
                    return redirect("/login")

                        
                

            
            
                return render(request,"signup.html",{"year":2022})

        def thanks(self,request):
            if request.user.is_authenticated:
                
                return render(request,"popup.html")
            
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")
            
        
        def cart(self,request,foodcode,):

            if request.user.is_authenticated:

                if request.method == 'POST':
                    if request.POST.get('remall'):
                        pass
                    cc = Cart.objects.all()
                    for i in cc:
                        if i.user_name == request.session['name']:
                            if i.code == int(foodcode):
                                if i.quantity >= 1:
                                    i.quantity = i.quantity - 1
                                    i.save()
                                    return redirect("/")

                f = Dishes.objects.get(pk=foodcode)
                cc = Cart.objects.all()
                for i in cc:
                    if i.user_name == request.session['name']:
                        if i.name == f.name:
                            i.quantity = i.quantity + 1
                            i.save()
                        
                        
                            return redirect("/dishes")
                
                
                
                
                c = Cart()
                c.user_name = request.session['name']
                c.name = f.name
                c.code = f.code
                c.img  = f.img
                                
                c.prise = f.prise
                c.quantity = 1
                c.save()
                connn = Cart.objects.all()

                
                m_ = []
                for i in connn:
                        if i.user_name == request.session['name']:
                            m_.append(i)

                sum = 0
                for i in m_:
                    sum = sum+i.prise
                ship = int(sum / 100) * 2
                pres = int(sum / 100) * 5
                total = int(sum / 100) * 5  + sum + ship   
                conn = {"sum":sum,"conn":m_,"total_prise":total, "pres":pres,"ship":ship}                
                return render(request,"cart.html",conn)

            else:
                return HttpResponse("<h1>NET Error... NOT allowed......</h1>")

        def show_cart(self,request):
            if request.user.is_authenticated:
                c = Cart.objects.all()
                m_ = []
                for i in c:
                    if i.user_name == request.session['name']:
                        m_.append(i)
                sum = 0

                for i in m_:
                    sum = sum+i.prise
                ship = int(sum / 100) * 2
                pres = int(sum / 100) * 5
                total = int(sum / 100) * 5  + sum  + ship                 
                conn = {"sum":sum,"conn":m_,"total_prise":total, "pres":pres,"ship":ship}  
                return render(request,"cart.html",conn)
            else:
                return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

                    
        def face_book(self,request):

            return redirect("/www.facebook.com")
        def twi_tter(request):

            return redirect("/www.twitter.com")

        def insta_gram(request):

            return redirect("/www.instagram.com")

        def beha_nce(request):
            return redirect("/www.behance.com" )

        def profile(self,request):
           
            if request.user.is_authenticated:
                return render(request,"profile.html")
            return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def searchh(self,request):
            if request.user.is_authenticated:
                if request.method == 'POST':
                    search_element = request.GET.get('search')
                    dishes_ = Dishes.objects.all()
                    dish_len = len(dishes_)
                    
                    menu_ = Menu.objects.all()
                    menu_len = len(menu_)

                    sp_dish = specialdish.objects.all()
                    spd_len = len(sp_dish)
                    for i in range(7,19):
                            obj_ = Dishes.objects.get(pk=i)
                            counter = 0
                        #if len(obj_.name) <= len(str(search_element)):
                            for i in obj_.name:
                                for j in str(search_element):
                                    if i == j:
                                        counter = counter + 1
                            if counter >= 1:
                                se_ar_h = Searchhhh()
                                se_ar_h.sear = str(search_element)
                                se_ar_h.save()
                    so = Searchhhh.objects.all()
                    return render(request,"search.html",{"output":so})


                
            
                return render(request,"search.html")
            else:
                return HttpResponse("<h1>NET Error... NOT allowed...</h1>")

        def logout(self,request,):
            
            auth.logout(request)
            
            return redirect("/login")
            
        def order_hist(self,request):
            if request.user.is_authenticated:
                name = request.session['name']
                or_der = Order.objects.all()
                collect = []
                for i in or_der:
                    if i.name == name:
                        collect.append(i)
                return render(request,"order_hist.html",{"order_details":collect})
            return HttpResponse("<h1>NET Error...  NOT allowed......</h1>")         
class navs:
    def navbar(self,request,nav):

        if nav == "dishes":
           return redirect("/dishes")
        elif nav == "menu":
            return redirect("/menu")
        elif nav == "review":
 
           return redirect("/review")
        
        elif nav == "about":

            return redirect("/about")
        elif nav == "order":

            return redirect("/order")

        elif nav == "search":

            return redirect("/search")
        elif nav == "home":
            return redirect("/index")
        elif nav == "signup":
            return redirect("/signup")
        elif nav == "login":
            return redirect("/login")
        elif nav == "www.facebook.com":
            pass
        elif nav == "logout":
            return redirect("/logout")
        elif nav == "profile":
            return redirect("/profile")
        else:
            pass



