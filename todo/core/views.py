from django.shortcuts import render
from .models import todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add(request):
    form = TodoForm()
    return render(request, 'todo/add.html', {'form': 'form'})
