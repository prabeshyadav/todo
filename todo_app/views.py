from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    tasks= task.objects.all()
    form= TaskForm()
    
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    
    
    context ={'tasks':tasks,'form':form}

    
    
    return render(request,'current/list.html',context)

def update_task(request,pk):
    task= task.object.get(id=pk)
    
    form=TaskForm(instance=task)
    
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'current/updated.html',context)
        