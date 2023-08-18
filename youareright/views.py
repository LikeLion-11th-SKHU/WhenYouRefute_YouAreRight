from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm
from django.utils import timezone
from .models import Post, Hashtag
from .forms import PostForm
from django.db.models import Q

# Create your views here.


def main(request):
    current_week = timezone.now().isocalendar()[1]

    # rommmu :: Hashtag filtering
    for hashtags in Hashtag.objects.all():
        if current_week != hashtags.hash_date.isocalendar()[1]:
            hashtags.count = 0
            hashtags.save()
    post = Post.objects.all().order_by("-likes")[:3]
    hashtag = Hashtag.objects.filter(count__gt=0).order_by("-count")[:6]
    return render(request, "main.html", {"hashtag": hashtag, "post": post})


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
                if word[0] == "#":
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    # rommmu :: hashtag 가 작성될 때 hash_date에 현재를 저장
                    hashtag.hash_date = timezone.now()
                    if not created:
                        hashtag.count += 1
                    hashtag.save()
                    form.hashtags.add(hashtag)
            return redirect("board")
    else:
        form = PostForm()
        return render(request, "create.html", {"form": form})


def board(request):
    post = Post.objects.all()
    return render(request, "board.html", {"post": post})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.count += 1
    post.save()
    return render(request, "detail.html", {"post": post})


def update(request, id):
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


def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("board")


# 해시태그 페이지
def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    boards = hashtag.post_set.order_by("-pk")
    return render(request, "hashtag.html", {"hashtag": hashtag, "boards": boards})


# 좋아요 함수
def like(request, pk):
    if not request.user.is_active:
        return HttpResponse("로그인이 필요합니다.")

    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect("detail", pk)


def search(request):
    search_item = request.GET.get("search_item")
    if search_item:
        post_list = (
            Post.objects.all()
            .filter(
                Q(title__icontains=search_item)  # 제목 검색
                | Q(body__icontains=search_item)  # 내용 검색
                | Q(user_name__icontains=search_item)  # 질문 글쓴이 검색  # 답변 글쓴이 검색
            )
            .distinct()
        )
        return render(request, "search.html", {"post_list": post_list})
