# urls.py is where we set up the templates (pages) -J
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]