from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('about/', views.about, name='main-about')
]