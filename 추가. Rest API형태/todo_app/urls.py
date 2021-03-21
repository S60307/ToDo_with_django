from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index ,name="index"),
    path('create',views.createTodo,name="create"),
    path('delete/<int:todo_id>',views.deleteTodo,name="delete"),
    path('update/<int:todo_id>',views.updateTodo,name="update"),
    path('detail/<int:todo_id>',views.detailTodo,name="detail"),
    # path('like/', views.applyTodo, name='applyTodo'),
]
