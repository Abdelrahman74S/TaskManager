from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Task
from .forms import TaskForm, updateTask  
def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_task.html', context={'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})  


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = updateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = updateTask(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('list_task')
    return render(request, 'tasks/delete_task.html', {'task': task})


def detail_task(request, id): 
    task = get_object_or_404(Task, id=id)
    return render(request, 'tasks/detail_task.html', {'task': task})  

def sort_task(request):
    sorted_objects = Task.objects.all().order_by('-created_at', 'status', 'title')
    context = {'tasks': sorted_objects}
    return render(request, 'tasks/sort_task.html', context)


def search_task(request):
    query = request.GET.get('q', '')
    results = Task.objects.none()

    if query:
        results = Task.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'tasks/search_task.html', context)
