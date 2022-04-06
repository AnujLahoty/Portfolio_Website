from django.shortcuts import render,get_object_or_404
from . import models
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = models.Blog.objects.order_by('-date')
    no_of_blogs = len(blogs)
    return render (request, 'blog/all_blogs.html', {'blogs':blogs, 'no_of_blogs':no_of_blogs}) 

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})