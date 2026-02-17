from django.contrib import admin
from .models import Author, Tag, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date')
    list_display = ('title', 'date', 'author')
    prepopulated_fields = {"slug": ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user_name', 'post')
    list_filter = ('user_name',)

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
