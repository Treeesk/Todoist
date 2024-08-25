from django import forms
from .models import Today

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Today
        fields = ['tasks']
        widgets = {
            'tasks': forms.Textarea()
        }
