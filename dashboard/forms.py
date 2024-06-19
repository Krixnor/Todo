from django import forms
from django.contrib.auth.models import User
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter activity', 'class':'form-control'}))


    class Meta:
        model = Todo
        fields = ['title']
    
