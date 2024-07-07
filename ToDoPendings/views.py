# Create your views here.
from django.shortcuts import render, redirect
from .forms import TodoForm
from django.contrib.auth.models import User

def create_todo(request):
    users = User.objects.all()
    message = None  # Inicializa un mensaje como nulo al principio

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            message = '¡creado correctamente!'  # Establece el mensaje de éxito
            # return redirect('todo_created')
    else:
        form = TodoForm()
    
    return render(request, 'create_todo.html', {'users': users, 'form': form, 'message': message})


def todo_created(request):
    return render(request, 'todo_created.html')
