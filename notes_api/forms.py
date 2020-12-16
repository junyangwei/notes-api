from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    """笔记"""
    class Meta:
        model = Notes
        fields = ['title', 'content']
        label = {
            'title': '',
            'content': '',
        }
