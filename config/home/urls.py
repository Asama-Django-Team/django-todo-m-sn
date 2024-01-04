from django.contrib import admin
from django.urls import path, include
from .views import intro

urlpatterns = [
    path('', intro),
]