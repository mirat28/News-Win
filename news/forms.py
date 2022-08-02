from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = Task
        # fields = ["title", "task"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок Новости'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание Новости'
        }),
        }

