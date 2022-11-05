from multiprocessing import context
from pickletools import read_unicodestring1
from unicodedata import name
from django.shortcuts import render

from base.models import Service

# Create your views here.
def home(request):
    services = Service.objects.all()
    
    context = {'services':services}
    return render(request, 'base/home.html',context)


def service(request,pk):
    services = Service.objects.get(id=pk)
    context = {'services':services}
    return render(request, 'base/service.html',context)

def about(request):
    context = {}
    return render(request,'base/about.html',context )


