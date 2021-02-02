from django.forms import ModelForm
from .models import Todo
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields ={'title', 'sex' , 'city' ,'level' ,'schedule','number','time' }
        widgets = {
            'schedule' : DateInput()
        }