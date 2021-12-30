from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Create your models here.
class AboutMe(models.Model):
    Bio = models.TextField(max_length=200)
    image_address = models.CharField(max_length=50)
    def __str__(self):
        return "About Me"

class specialities(models.Model):
    name         = models.CharField(max_length=15)
    Date_Of_earn = models.DateField(auto_now=False, auto_now_add=False)
    Description  = models.TextField(max_length=200)
    def __str__(self):
        return "{}-{}".format(self.name, self.Date_Of_earn)

class Experiences(models.Model):
    name         = models.CharField(max_length=15)
    Date_Of_Earn = models.DateField(auto_now=False, auto_now_add=False)
    Description  = models.TextField(max_length=200)
    def __str__(self):
        return "{}-{}".format(self.name, self.Date_Of_Earn)

class Academy(models.Model):
    name               = models.CharField(max_length=15)
    Degree             = models.CharField(max_length=15)
    Date_Of_Graduation = models.DateField(auto_now=False, auto_now_add=False)
    Description        = models.TextField(max_length=200)
    def __str__(self):
        return "{}-{}".format(self.name, self.Degree)
 

class contact(models.Model):
    Email   = models.EmailField()
    name    = models.CharField(max_length=15)
    Message = models.TextField(max_length=300)
    def __str__(self):
        return "{}-{}".format(self.name, self.Email)

class Economy(models.Model):
    user               = models.ForeignKey(User, on_delete=CASCADE)
    E_ID               = models.AutoField(primary_key=True)
    Description        = models.TextField(max_length=200)
    category           = models.CharField(max_length=20)
    Amount             = models.PositiveIntegerField()
    def __str__(self):
        return "{}-{}-{}".format(self.category, self.user, self.Amount)

class ToDoer(models.Model):
    user          = models.ForeignKey(User, on_delete=CASCADE)
    T_ID          = models.AutoField(primary_key=True)
    Task          = models.CharField(max_length= 20) 
    Task_category = models.CharField(max_length= 20)
    Deadline      = models.DateField(auto_now=False, auto_now_add=False)
    Description   = models.TextField(max_length=200)
    def __str__(self):
        return "{}-{}-{}".format(self.Task, self.user, self.Task_category)