from atexit import register
from django.contrib import admin
from .models import Category, Post
from .models import Comment, Like, PostView



# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Comment)