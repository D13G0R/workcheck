from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25, blank = False, null = False)
    color = models.CharField(max_length=10, blank = False, null = False)
    