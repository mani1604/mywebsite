from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string

blog_names = {
    "python-intro": "Introduction to Python",
    "django-basics": "Django basics",
    "python-oops": "OOPs in Python",
    "react": "UI with HTML, CSS & React"
}

# Create your views here.
def blogposts(request):
    blog_list = list(blog_names.keys())    
    return render(request, "blogs/allposts.html", {"blogs" : blog_list})

def home_page(request):
    return render(request, "blogs/index.html")

def process_blog_name(blog):
    # django-basics => Django Basics
    return blog.replace("-", " ")

def blog_post(request, blog):
    try:
        content = blog_names[blog]
    except Exception:
        raise Http404()
    else:
        return render(request, "blogs/posts.html", {"blog_text": content, "blog_name": process_blog_name(blog)})
