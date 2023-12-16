from django import forms 
from .models import TaskCategorys


class CategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategorys
        fields = '__all__'