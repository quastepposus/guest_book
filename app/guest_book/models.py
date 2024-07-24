from django.contrib import admin
from django.db import models


class Post(models.Model):
    author_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Author Name")
    author_mail = models.EmailField(max_length=200, null=False, blank=False, verbose_name="Author Email")
    text = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Post Text")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="Edit Time")
    choices = (('active', 'active'), ('blocked', 'blocked'))
    status = models.CharField(default='active', choices=choices, max_length=50, verbose_name="Status")


class AdminPost(admin.ModelAdmin):
    list_display = ['author_name', 'author_mail', 'create_time', 'edit_time', 'status']
    list_filter = ['status']
    fields = ['author_name', 'author_mail', 'text', 'create_time', 'edit_time', 'status']
    search_fields = ['author_name', 'author_mail']
    readonly_fields = ['create_time', 'edit_time']
