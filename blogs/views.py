from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime


blog_details = [
    {
        'slug': 'python-intro',
        'title': 'Introduction to Python',
        'image': 'python.jpg',
        'preview': 'Python is a high level programming language',
        'content': """ Python is a high-level, interpreted, and general-purpose programming language known for its simple, easy-to-read syntax that emphasizes readability. Created by Guido van Rossum in 1991, it is widely used for web development, artificial intelligence, data science, and automation. It is beginner-friendly and supports multiple programming paradigms, including structured and object-oriented programming. """,
        'date': datetime( 2026, 2, 11),
    },
    {
        'slug': 'django-basics',
        'title': 'Introduction to Django',
        'image': 'django.png',
        'preview': 'Python is a web framework',
        'content': """ Django is a high-level, open-source Python web framework that encourages rapid development and clean, pragmatic design. It provides a full set of components and built-in features, often described as "batteries included," so developers can focus on building unique application features rather than repetitive boilerplate code.  """,
        'date': datetime( 2026, 2, 12),
    },
    {
        'slug': 'react',
        'title': 'React Introduction',
        'image': 'react.png',
        'preview': 'ReactJS for UI',
        'content': """ ReactJS is a component-based JavaScript library used to build dynamic and interactive user interfaces. It simplifies the creation of single-page applications (SPAs) with a focus on performance and maintainability.  """,
        'date': datetime( 2026, 2, 10),
    },
]

def home_page(request):
    sorted_blogs = sorted(blog_details, key=lambda x: x['date'], reverse=True)
    latest_blogs = sorted_blogs[:2]
    return render(request, 'blogs/index.html', {'l_blogs': latest_blogs})           


def blogposts(request):
    return render(request, 'blogs/allposts.html', {"blogs": blog_details})


def process_blog_name(blog):
    #django-basics -> Django Basics
    return blog.replace("-"," ")


def blog_post(request, blog):
    try:
        for post in blog_details:
            if post['slug'] == blog:
                details = post
                break
        else:
            raise Http404()     
    except Exception:
        raise Http404()
    else:
        return render(request, 'blogs/posts.html', {'post_details': details})