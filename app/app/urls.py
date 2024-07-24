"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from guest_book.views import posts_view, create_post_view, edit_post_view, delete_post_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', posts_view, name='index'),
    path('posts', posts_view, name='posts'),
    
    path('posts/create', create_post_view, name='create_post'),
    path('posts/<int:pk>/edit', edit_post_view, name='edit_post'),
    path('posts/<int:pk>/delete', delete_post_view, name='delete_post'),
]
