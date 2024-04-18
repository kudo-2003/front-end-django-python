from django.shortcuts import render
from .models import Post

def introduce(request):
    return render(request, 'pages/home.html')


def list(request):
    Data = {'Posts': Post.objects.all()}
    return render(request, 'blog/blog.html', Data)