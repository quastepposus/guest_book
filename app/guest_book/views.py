from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404

from guest_book.models import Post


def posts_view(request):
    posts = Post.objects.all().filter(status='active').order_by('-create_time')
    return render(request, 'posts.html', context={'posts': posts})


def create_post_view(request):
    if request.method == 'GET':
        return render(request, 'create_post.html')
    elif request.method == 'POST':
        errors = {}

        author_name = request.POST.get('author_name')
        author_mail = request.POST.get('author_mail')
        text = request.POST.get('text')
        print(text)

        if not author_name:
            errors['author_name'] = 'author name is required'
        elif len(author_name) < 5:
            errors['author_name'] = 'author name is too short'

        if not author_mail:
            errors['author_mail'] = 'author mail is required'

        if not text:
            errors['text'] = 'text is required'
        elif len(text) < 20:
            errors['text'] = 'text is too short'
        elif len(text) > 2000:
            errors['text'] = 'text is too long'

        post = Post()
        post.author_name = author_name
        post.author_mail = author_mail
        post.text = text

        if len(errors) > 0:
            return render(request, 'create_post.html', context={'errors': errors, 'post': post})

        else:
            post.save()

            return redirect('posts')


def edit_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        return render(request, 'edit_post.html', context={'post':post})
    elif request.method == 'POST':
        errors = {}

        author_name = request.POST.get('author_name')
        author_mail = request.POST.get('author_mail')
        text = request.POST.get('text')

        if not author_name:
            errors['author_name'] = 'author name is required'
        elif len(author_name) < 5:
            errors['author_name'] = 'author name is too short'

        if not author_mail:
            errors['author_mail'] = 'author mail is required'

        if not text:
            errors['text'] = 'text is required'
        elif len(text) < 20:
            errors['text'] = 'text is too short'
        elif len(text) > 2000:
            errors['text'] = 'text is too long'

        post.author_name = author_name
        post.author_mail = author_mail
        post.text = text

        if len(errors) > 0:
            return render(request, 'edit_post.html', {'errors': errors, 'post': post})

        else:
            post.save()
            return redirect('posts')


def delete_post_view(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect('posts')

