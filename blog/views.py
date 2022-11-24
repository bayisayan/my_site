from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})


class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'detail'
