from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    # image = models.ImageField(max_length=100)   #run command "python -m pip install Pillow"
    image = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
