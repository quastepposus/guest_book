from django.contrib import admin

from guest_book.models import AdminPost, Post

# Register your models here.

admin.site.register(Post, AdminPost)
