from django.shortcuts import render, HttpResponse, redirect
from .models import User
import datetime

# Create your views here.
def index(request):
    context = {
        'context_list': User.objects.all().values()
    }
    return render (request, 'index.html', context)

def new(request):    
    return render (request, 'new.html')

def edit(request,id):
    context = {
        'context_list': User.objects.get(id=id)
    }
    return render (request, 'edit.html' , context)

def show(request,id):
    context = {
        'context_list': User.objects.get(id=id)
    }
    return render (request, 'show.html', context)

def create(request):
    if request.method == 'POST':
        U = User.objects.create(first_name =request.POST['first_name'] , last_name =request.POST['last_name'] , email =request.POST['email'])
    return redirect('/users/'+str(U.id))

def destroy(request,id):
    a = User.objects.get(id=id)
    a.delete()
    return redirect(index)

def update(request,id):
    if request.method == 'POST':
        a = User.objects.get(id=id)
        a.first_name = request.POST['first_name']
        a.last_name = request.POST['last_name']
        a.email = request.POST['email']
        a.updated_d = datetime.datetime.now()
        print("heloooooooooooooooooooooooo", a.updated_d)
        a.save()
    return redirect('/users/'+id)

    