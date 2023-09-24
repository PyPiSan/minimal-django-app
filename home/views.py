from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# default home view
def homepage(request, *args, **kwargs):
    return render(request, 'home.html')