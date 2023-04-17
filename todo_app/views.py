from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks= task.objects.all()
    form = taskForm()
    context ={'tasks':tasks,'form':form}

    
    
    return render(request,'current/list.html',context)