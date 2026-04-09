from django import forms
from apps.category.models import Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["title", "color"]
