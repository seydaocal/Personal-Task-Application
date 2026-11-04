from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_POST

from .forms import TaskForm, CategoryForm
from .models import Task, Category


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required

def task_list(request):
    tasks = Task.objects.filter(user=request.user).select_related("category")
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")
    category_id = request.GET.get("category", "")

    if q:
        tasks = tasks.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if status:
        tasks = tasks.filter(status=status)
    if category_id.isdigit():
        tasks = tasks.filter(category_id=category_id)

    context = {
        "tasks": tasks,
        "categories": Category.objects.filter(user=request.user),
        "status_choices": Task.status_choices,
        "q": q,
        "selected_status": status,
        "selected_category": category_id,
    }
    return render(request, "tasks/task_list.html", context)

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
    else:
        form = TaskForm(user=request.user)
    return render(request, "tasks/task_form.html", {"form": form, "title": "Yeni Görev"})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, "tasks/task_form.html", {"form": form, "title": "Görevi Düzenle"})


@login_required
@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect("home")


@login_required
@require_POST
def task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = "done"
    task.save()
    return redirect("home")


@login_required

def category_list(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    categories = Category.objects.filter(user=request.user)
    return render(request, "tasks/category_list.html", {"categories": categories, "form": form})


@login_required
@require_POST
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    category.delete()
    return redirect("category_list")

