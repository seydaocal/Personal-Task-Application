from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="home"),
    path("register/", views.register, name="register"),
    path("tasks/new/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task_update"),
    path("tasks/<int:pk>/done/", views.task_done, name="task_done"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:pk>/delete/", views.category_delete, name="category_delete"),

]