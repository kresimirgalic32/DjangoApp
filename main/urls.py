from os import name
from django.conf.urls import url
from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name = "home"),
path("create/", views.create, name = "create")
]