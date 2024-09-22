from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from .forms import TaskForm 
# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# Password Reset View
def password_reset_view(request):
    return render(request, 'tasks/password.html')

# Tables View
def tables_view(request):
    return render(request, 'tasks/tables.html')
# Task List View (à ajouter)
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
    # Task Create View
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks/task_list')  # Redirection vers la liste des tâches
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})
    # Task Update View
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks/task_list.html', {'tasks': tasks})  # Redirection après la mise à jour
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form})

# Task Delete View
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks/task_list')  # Redirection après la suppression
    return render(request, 'tasks/task_delete.html', {'task': task})
