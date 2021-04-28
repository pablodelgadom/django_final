from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from registration import views

urlpatterns = [
    path('registro', views.SignupView.as_view(), name = "registro"),
    path('logout', views.logout),
    path('profile/',views.UserEditView.as_view(), name= 'edit_profile'),
]