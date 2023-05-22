from django import forms
from .models import Task


class AddForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "title of the task"
    }))
    completed = forms.BooleanField()
    
    class Meta:
        model = Task
        fields = [
            'title','completed'
        ]