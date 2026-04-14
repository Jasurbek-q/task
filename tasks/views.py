from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Task
from .forms import TaskForm, RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})


@login_required
def task_list(request):
    status_filter = request.GET.get('status', '')
    tasks = Task.objects.filter(user=request.user)
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    status_choices = Task.STATUS_CHOICES
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'status_filter': status_filter,
        'status_choices': status_choices,
    })


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Edit'})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
