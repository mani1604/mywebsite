from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime
from .models import Post

def home_page(request):
    latest_blogs = Post.objects.all().order_by("-date")[:2]
    return render(request, 'blogs/index.html', {'l_blogs': latest_blogs})           


def blogposts(request):
    blog_details = Post.objects.all()
    return render(request, 'blogs/allposts.html',
                   {"blogs": blog_details})


def process_blog_name(blog):
    #django-basics -> Django Basics
    return blog.replace("-"," ")


def blog_post(request, blog):
    try:
        details = Post.objects.get(slug=blog)
        tags = details.tags.all()
    except Exception:
        raise Http404()
    else:
        return render(request, 'blogs/posts.html', 
                      {'post_details': details, 'tags': tags})
