from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index ,name="index"),
    path('createTodo/',views.createTodo,name="createTodo"),
    path('<int:todo_id>/deleteTodo/',views.deleteTodo,name="deleteTodo"),
    path('<int:todo_id>/updateTodo/',views.updateTodo,name="updateTodo"),
    path('<int:todo_id>/',views.detailTodo,name="detailTodo"),
    path('like/', views.applyTodo, name='applyTodo'),
]
