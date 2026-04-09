from django.contrib import admin
from django.urls import path, include
from .views import home, list_tasks, delete_task, update_task

urlpatterns = [
    path("", home, name = "home"),
    path("list/", list_tasks.as_view(), name = "list_tasks"),
    path("delete/<int:id>", delete_task, name = "delete_task"),
    path("update/<int:id>", update_task, name = "update_task")

]