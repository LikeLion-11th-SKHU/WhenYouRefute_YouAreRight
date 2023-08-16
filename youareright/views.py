from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.utils import timezone
from .models import Post, Hashtag
from .forms import PostForm

# Create your views here.


def main(request):
    hashtag = Hashtag.objects.order_by('-count')[:3]
    return render(request, "main.html", {"hashtag":hashtag})


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.count = 0
            form.save()
            # 해시태그
            for word in form.body.split():
                if word[0] == '#':
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    if not created:
                        hashtag.count += 1
                        hashtag.hash_date = timezone.datetime.now()
                        hashtag.save()
                    form.hashtags.add(hashtag)
            return redirect("board")
    else:
        form = PostForm()
        return render(request, "create.html", {"form": form})
    
def board(request):
    post = Post.objects.all()
    return render(request, "board.html", {"post": post})


def detail(request, title):
    post = get_object_or_404(Post, id=id)
    post.count += 1
    post.save()
    return render(request, "detail.html", {"post": post})


def update(request, title):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect("board")
    else:
        form = PostForm(instance=post)
        return render(request, "update.html", {"form": form})


def delete(request, title):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("board")


# 해시태그 페이지
def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    boards = hashtag.post_set.order_by('-pk')
    return render(request, 'hashtag.html', {'hashtag': hashtag, 'boards': boards})
