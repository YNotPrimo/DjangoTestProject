from django.urls import path
from tstApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
