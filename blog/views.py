from django.shortcuts import render

# from .templates import *

posts = [
    {
        "author": "Raushan Singh",
        "title": "Blog Post1",
        "content": "This is my First Post on Django"
                   "Framework. This blog tells about Blogging.",
        "date_posted": "August 24, 2019"

    },
    {
        "author": "Avinash Singh",
        "title": "Blog Post2",
        "content": "This is my Second Post on Django"
                   "Framework. This blog tells about Blogging.",
        "date_posted": "August 24, 2019"

    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Raushan'})


def Register(request):
    return render(request, 'blog/register.html')


def Login(request):
    return render(request, 'blog/login.html')
