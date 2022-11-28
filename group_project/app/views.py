#views.py is where we make our http requests and database queries using ORM -J
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
