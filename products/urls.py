from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage),
    path("new", views.newProducts)
]
