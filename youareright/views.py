from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post

# Create your views here.


def index(request):
    return render(request, "board.html")


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.count = 0
            form.save()
            return redirect("read")
    else:
        form = PostForm()
        return render(request, "create.html", {"form": form})


def read(request):
    post = Post.objects.all()
    return render(request, "read.html", {"post": post})


def detail(request, title):
    post = get_object_or_404(Post, title=title)
    post.count += 1
    post.save()
    return render(request, "detail.html", {"post": post})


def update(request, title):
    post = get_object_or_404(Post, title=title)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect("read")
    else:
        form = PostForm(instance=post)
        return render(request, "update.html", {"form": form})


def delete(request, title):
    post = get_object_or_404(Post, title=title)
    post.delete()
    return redirect("read")
