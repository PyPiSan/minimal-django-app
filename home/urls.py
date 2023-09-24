from django.urls import path # path is just like adding directory
from . import views

urlpatterns =[
    path('', views.homepage),
]

