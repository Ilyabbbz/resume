from django.contrib import admin
from django.urls import path, include
from . import views
from my_site import my_app


urlpatterns = [
    path('', my_app.views.index, name='index'),
]