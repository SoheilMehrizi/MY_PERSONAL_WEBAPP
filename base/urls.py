from django.urls import path
from base import views
urlpatterns = [
    path('', views.Home, name="Home"),
    path('Home', views.Home, name="Home"),
    path('Specialities', views.Specialities, name="Specialities"),
    path("Expriences", views.Expriences, name="Expriences"),
    path("Academy", views.Academy_View, name="Academy"),
    path("Contact", views.Contact, name="Contact"),
    path("Bio", views.Bio, name="Bio"),
    path("CV", views.CV, name="CV"),
    path("Profile", views.Profile, name="Profile"),
    path("LogIn", views.LogIn, name="LogIn"),
    path("LogOut", views.LogOut, name="LogOut"),
    path("Economy", views.economy, name="Economy"),
    path("Todoer", views.todoer, name="Todoer"),
    path("Task_view", views.Task_view, name="Task_view"),
]
