from django.urls import path
from partTwoExercise import views

urlpatterns = [
    path('', views.users, name='users'),
]