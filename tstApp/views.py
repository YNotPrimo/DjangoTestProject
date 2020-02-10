from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    dct = {'index': "https://youtu.be/OkNw95QAaco"}
    return render(request, 'tstApp/index.html', context=dct)
