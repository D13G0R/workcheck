from django.urls import path, include
from apps.category.views import ListCategories, CreateCategory, DeleteCategory, UpdateCategory

urlpatterns = [

    path("list/", ListCategories.as_view(), name = "list_categories"),
    path("create/", CreateCategory.as_view(), name = "create_category"),
    path("delete/<int:pk>", DeleteCategory.as_view(), name = "delete_category"),
    path("update/<int:pk>", UpdateCategory.as_view(), name = "update_category")
]
