from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.single_blog, name='single_blog'),
    ]
