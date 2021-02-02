from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
#from django.http import HttpResponse,HttpResponseRedirect

def signup(request):
    if request.method =="POST":
        if request.POST["password1"] == request.POST["password2"]:
            user =User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
            auth.login(request,user)
            return redirect('index')
        return render(request,'todo_customer/signup.html')

    return render(request,'todo_customer/signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request, 'todo_customer/login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request,'todo_customer/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

# Create your views here.
