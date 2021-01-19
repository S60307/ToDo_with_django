from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm  


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context={'todos':todos}
    return render(request,'todo_app/index.html',context)

def createTodo(request):
    new_todo= TodoForm(request.POST)
    new_todo.save()
    return HttpResponseRedirect(reverse("index"))


def deleteTodo(request):
    delete_todo_id=request.GET['id']
    todo=Todo.objects.get(id=delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def clearTodo(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))

def update(request):

    return HttpResponseRedirect(reverse('index'))

