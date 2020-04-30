from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'SpidersForEyes',
        'title': 'Blog Post 1',
        'content': 'First post content', 
        'date_posted': 'April 23, 2020'
    },
    {
        'author': 'SpidersForEyes',
        'title': 'Blog Post 2',
        'content': 'Second post content', 
        'date_posted': 'April 24, 2020'
    }
]

# Create your views here.
def home(request):
    '''
    routes traffic to home page
    '''
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
