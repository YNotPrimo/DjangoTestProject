from django.shortcuts import render
from tstApp.models import AccessRecord
from . import forms


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'tstApp/index.html', context=date_dict)
