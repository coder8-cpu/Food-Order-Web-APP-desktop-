from distutils.command.upload import upload
from tokenize import cookie_re
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=30) #
    desc = models.CharField(max_length=30)
    prise = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    code = models.IntegerField()
    

class Menu(models.Model):
    name = models.CharField(max_length=30) #
    desc = models.CharField(max_length=30)
    prise = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    code = models.IntegerField()


class Review(models.Model):
    name = models.CharField(max_length=30)
    rev = models.TextField()


class Order(models.Model):
    name = models.CharField(max_length=20)
    mobileno = models.IntegerField()
    food_name = models.CharField(max_length=20)
    extra_food = models.CharField(max_length=20)
    count = models.IntegerField()
    address = models.TextField()
    msg = models.TextField()
    code = models.CharField(max_length=20)

class specialdish(models.Model):
    name = models.CharField(max_length=30) #
    desc = models.CharField(max_length=30)
    img = models.ImageField(upload_to='pics')
    code = models.IntegerField()
    prise = models.IntegerField()

class Cart(models.Model):
    user_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    prise = models.IntegerField()
    quantity = models.IntegerField()
class Signup(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=12)
    c_pwd = models.CharField(max_length=12)
 

class Login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=12)
    active = models.IntegerField()
    
 
class Searchhhh(models.Model):
    sear = models.CharField(max_length=30)

class Active(models.Model):
    active_token = models.IntegerField()
    


    
