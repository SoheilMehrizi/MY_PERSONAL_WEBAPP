from json import encoder
from django.contrib.auth.backends import UserModel
from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from base.models import AboutMe, Economy, Experiences, ToDoer, contact, specialities
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
# Create your views here.
def Home(request):
    try:
        Bio_Model = AboutMe.objects.all()[0]
        Bio_Text  = Bio_Model.Bio
        Bio_Image = Bio_Model.image_address
        SPEIS = specialities.objects.all()
        experiences = Experiences.objects.all()
        academies = Academy.objects.all()
        return render(request, "base/home.html", context={
            "Bio" : Bio_Text,
            "Image_URL" : Bio_Image,
            "SPEIS" : SPEIS,
            "experiences":experiences,
            "academies":academies,
        })
    except IndexError:
        return render(request, "base/home.html", context={
            "resualt":"Failed",
        })

def Specialities(request):

    try:
        SPEIS = specialities.objects.all()
        return render(request, "base/specialities.html", context={
            "SPEIS" : SPEIS
        })         
    except IndexError:
        return render(request, "base/specialities.html", context={
            "resualt":None,
    })

def Expriences(request):
    try:
        experiences = Experiences.objects.all()
        return render(request, "base/experiences.html", context={
        "experiences":experiences,
        })
    except IndexError:
        return render(request, "base/experiences.html", context={
        "resualt":None,
        })
from base.models import Academy
def Academy_View(request):
    try:
        academies = Academy.objects.all()
        return render(request, "base/academy.html", context={
        "academies":academies,
        })
    except IndexError:
        return render(request, "base/academy.html", context={
        "resualt":None,
        })

#Take Contacts Messages To My Email
def Contact(request):
    if request.method == "POST":
        email   = request.POST["email"]
        message = request.POST["message"]
        contact.objects.create(Email = email, name = "Empty", Message = message)
        return render(request, "base/home.html", context={
            "resualt" : "message sent successfuly."
        })
    else:
        return render(request, "base/contact.html", context={
        "resualt":None,
        })

#Returnning the content Of Bio

def Bio(request):
    try:    
        Bio_Model = AboutMe.objects.all()[0]
        Bio_Text  = Bio_Model.Bio
        Bio_Image = Bio_Model.image_address
        print(f"Bio Text : {Bio_Text} \n Bio_Image : {Bio_Image} \n")
        return render(request, "base/Bio.html", context={
            "Bio" : Bio_Text,
            "Image_URL" : Bio_Image,
        })
    except IndexError:
        return render(request, "base/Bio.html", context={
            "Bio" : "DataBase Is Empty",
            "Image_URL" : "Database Is Empty",
        })

#Returning Response For CV Page
def CV(request):
    return render(request, "base/CV.html", context={
    "resualt":None,
    })

#Returning Response For Profile
T_category = ["College", "Essey", "Searching_Life", "Programming" , "Study_Books"]
E_category = ["Save", "Purchase_Saving", "SnappFood", "Junk Food", "Fares"]
@login_required(login_url="/LogIn")
def Profile(request):
    tasks = ToDoer.objects.all()
    return render(request, "base/profile.html", context={
    "tasks":tasks,
    "T_category" : T_category,
    "E_category" : E_category,
    "resualt":None,
    })

#Loging In User
def LogIn(request):
    if request.method == "POST":
        username = request.POST["Username"]
        password = request.POST["password"]
        user     = authenticate (request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/Home")
        else:
            return render(request, "base/login.html", context={
            "resualt":"FAILED",
            }) 
    else:
        return render(request, "base/login.html", context={
        "resualt":None,
        })

#Log Out User
def LogOut(request):
        logout(request)
        return redirect(Home)
# Add Economic Logs
@login_required(login_url="/LogIn")
def economy(request):
    print(request.user)
    if request.method == "POST":
        User        = request.user
        description = request.POST["Description"]
        category    = request.POST["Category"]
        if category not in E_category :
            return redirect("/Profile")
        amount      = request.POST["Amount"]
        Economy.objects.create(
            user = User,
            Description = description,
            category = category,
            Amount = int(amount),
            )   
        return redirect("/Profile#Economy-form")
    else:
        return redirect("/Profile")


#Add Todo Logs
@login_required(login_url="/LogIn")
def todoer(request):
    if request.method == "POST":
        User          = request.user
        task          = request.POST["Task"]
        task_category = request.POST["Task_Category"]
        if task_category not in T_category :
            return redirect("/Profile")
        deadline      = request.POST["Deadline"]
        description   = request.POST["Description"]
        ToDoer.objects.create(
            user = User,
            Task = task,
            Description = description,
            Task_category = task_category,
            Deadline = deadline,
            )   
        return redirect("/Profile")
    else:
        return redirect("/Profile")      

@login_required(login_url="/LogIn")
def Task_view(request):
    if request.method == "POST":
        try:
            tasks = ToDoer.objects.all()
            for tsk in tasks:
                task_name = tsk.Task
                print(request["taskstatus"])
            return render(request, "base/profile.html", context={
                "tasks":tasks
            })
        except TypeError:
            return redirect("/Profile")            


    else:
        tasks = ToDoer.objects.all()
        return render(request, "base/profile.html", context={
            "tasks":tasks
        })