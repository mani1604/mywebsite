from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import datetime
from .models import Post
from .forms import CommentForm

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
    form_data = CommentForm()

    try:
        details = Post.objects.get(slug=blog)
        tags = details.tags.all()
        all_comments = details.comments.all()
        if request.method == "POST":
            comment_data = request.POST
            form = CommentForm(comment_data)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = details
                comment.save()
                return HttpResponseRedirect(reverse("blog-post"), args=[blog])
            else:
                return render(request, 'blogs/posts.html', 
                      {'post_details': 
                       details, 'tags': tags,
                       'comment_form': form})
    except Exception:
        raise Http404()
    else:
        return render(request, 'blogs/posts.html', 
                      {'post_details': 
                       details, 'tags': tags,
                       'comment_form': form_data})
