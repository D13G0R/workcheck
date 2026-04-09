
from django.db import models
from django.core.validators import MinLengthValidator
from apps.category.models import Category
class Task(models.Model):
    title = models.CharField(max_length=100, validators = [MinLengthValidator(3)])
    description = models.TextField(blank=True)
    value = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1)