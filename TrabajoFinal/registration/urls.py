from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from registration import views

urlpatterns = [
    path('register', views.register_view, name = "register_view"),
    #path('login', views.login),
    path('logout', views.logout),
]