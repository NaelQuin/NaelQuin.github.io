from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.index , name="index"),
   # path('login'. views.login, name="login"),
   # path('Signout'. views.Signout, name="Signout"),
]
