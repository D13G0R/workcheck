from .models import Task
from .forms import TaskForm
from apps.category.models import Category

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from django.shortcuts import redirect


def home(request):
    return render(request, "home.html")

class list_tasks(ListView):
    model = Task
    template_name = "all_tasks.html"
    context_object_name = "tasks"
    
    def post (self, request, *args, **kwargs):

        title = request.POST.get("title")
        description = request.POST.get("description")
        value = request.POST.get("value")

        Task.objects.create(
            title = title,
            description = description,
            value = value
        )

        return redirect("tasks")

def delete_task(request, id):
    task = get_object_or_404(Task, id = id)

    if request.method == "POST":
        task.delete()
        return redirect("list_tasks")
    
    return render(request, "confirm_delete_task.html", {"task" : task})

def update_task(request, id):
    task = get_object_or_404(Task, id = id)
    categories = Category.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            
            return redirect("list_tasks")
    
    form = TaskForm(instance = task)
    return render (request, "update_task.html", {"form" : form, "categories" : categories}) 
