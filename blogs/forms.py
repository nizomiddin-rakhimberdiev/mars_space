from django import forms

from blogs.models import BlogPost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image']