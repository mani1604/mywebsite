from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    # image = models.ImageField(max_length=100)   #run command "python -m pip install Pillow"
    image = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=25)
    user_email = models.EmailField()
    comment_text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE,
                             related_name="comments")

