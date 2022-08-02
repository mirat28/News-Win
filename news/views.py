from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Article
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'news/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'news/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = ' Форма была не верной!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create_news.html', context)







