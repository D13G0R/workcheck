from django import forms
from apps.tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        fields = ["title", "description", "value", "category"]
        model = Task