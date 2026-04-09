from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.category.models import Category
from apps.category.forms import CategoryForm
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your view

class ListCategories(ListView):
    model = Category
    template_name = "categories.html"
    context_object_name = "categories"

class CreateCategory(CreateView):
    form_class = CategoryForm
    template_name = "create_category.html"
    success_url = reverse_lazy("list_categories")

class DeleteCategory(DeleteView):
    model = Category
    template_name = "confirm_delete_category.html"
    success_url = reverse_lazy("list_categories")

class UpdateCategory(UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = "update_category.html"
    success_url = reverse_lazy("list_categories")
    
    