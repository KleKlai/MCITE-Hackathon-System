from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
	
	"""
	links for the API endpoint
	"""
urlpatterns = [

    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
]