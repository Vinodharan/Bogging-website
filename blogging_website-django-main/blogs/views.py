from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-created_date')[:20]
    context = {
        'posts' : posts,
    }
    return render(request, 'blogs/home.html', context)


@login_required(login_url='login')
def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post,
    }
    return render(request, 'blogs/single_post.html', context)


def search(request):
    posts = Post.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        data = request.GET['keyword']
        if data:
            posts = posts.filter(body__icontains=data) | posts.filter(title__icontains=data)

    count = posts.count()
    context = {
        'posts' : posts,
        'count' : count,
    }
    return render(request, 'blogs/search.html', context)


@login_required(login_url='login')
def myblogs(request):
    current_user = request.user
    posts = Post.objects.filter(author=current_user.id)
    count = posts.count()
    context = {
        'posts' : posts,
        'count' : count,
    }
    return render(request, 'blogs/myblogs.html', context)


@login_required(login_url='login')
def addBlog(request):
    current_user = request.user
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newblog = Post(title=title, author=current_user, body=body)
        newblog.save()
        messages.success(request, 'Blog added successfully')
    
    return render(request, 'blogs/addblog.html')


@login_required(login_url='login')
def updateBlog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post' : post,
    }
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        post.title = title
        post.body = body
        post.save()
        messages.success(request, 'Blog updated successfully')
        return redirect('myblogs')
    return render(request, 'blogs/updateblog.html', context)


@login_required(login_url='login')
def deleteBlog(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Blog deleted succesfully')
    return redirect('home')
