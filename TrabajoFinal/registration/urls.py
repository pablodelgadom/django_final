from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from registration import views

urlpatterns = [
    path('registro', views.SignupView.as_view(), name = "registro"),
    #path('login', views.login),
    path('logout', views.logout),
    path('perfil/',views.UserProfileView.as_view(), name= 'user_profile')
]