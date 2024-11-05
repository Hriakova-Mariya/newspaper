from django import forms
from django.core.exceptions import ValidationError
from .models import Post, PostCategory


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'categoryType',
            'postCategory'
        ]
