from django.shortcuts import render,redirect, get_object_or_404
from .models import Today
from django.views.decorators.http import require_http_methods


def index(request):
    todos = Today.objects.all()
    return render(request, 'today.html', {'todos':todos})

@require_http_methods(['POST'])
def add(request):
    tasks = request.POST["tasks"]
    task = Today(tasks=tasks)
    task.save()
    return redirect('todoist:index')
                    
def delete(request, today_id):
    todo = get_object_or_404(Today, id=today_id)
    todo.delete()
    return redirect('todoist:index')

def update(request, today_id):
    todo = get_object_or_404(Today, id=today_id)
    todo.tasks = request.POST.get('tasks')
    todo.edit_mode = False
    todo.save()
    return redirect('todoist:index')

def edit(request, today_id):
    todo = get_object_or_404(Today, id=today_id)
    todo.edit_mode = True
    todo.save()
    return redirect('todoist:index')    

def close(request, today_id):
    todo = get_object_or_404(Today, id=today_id)
    todo.edit_mode = False
    todo.save()
    return redirect('todoist:index')