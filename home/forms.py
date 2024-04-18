from django import forms
from .models import Post
from django.template.defaulttags import widthratio

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'time_create',)
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'tieude'}),
            'content': forms.Textarea(attrs={'class': 'noidung'})
        }