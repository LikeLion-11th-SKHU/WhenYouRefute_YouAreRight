from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Board, Hashtag, Reply
from .forms import BoardForm


def main(request):
    hashtag = Hashtag.objects.order_by('-count')[:3]
    return render(request, "main.html", {"hashtag":hashtag})


def board(request):
    board_list = Board.objects.all()
    return render(request, "board.html", {"board_list": board_list})


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, "detail.html", {"board": board})


def write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.datetime.now()
            board.save()
            form.save_m2m()
            # 해시태그
            for word in board.content.split():
                if word[0] == '#':
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    if not created:
                        hashtag.count += 1
                        hashtag.hash_date = timezone.datetime.now()
                        hashtag.save()
                    board.hashtags.add(hashtag)
            return redirect('youareright:board')
    else:
        form = BoardForm()
        return render(request, 'write.html', {'form':form})
    
def update(request, board_id):
    board = get_object_or_404(Board, id = board_id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save(commit=False)
            form.pub_date = timezone.datetime.now()
            form.save()
            return redirect('youareright:detail', board_id=board.id)
    else:
        form = BoardForm(instance=board)
        return render(request, 'detail.html', {'form':form})


def delete(request, board_id):
    board = get_object_or_404(Board, id = board_id)
    board.delete()
    return redirect('youareright:board')



def create_reply(request, board_id):
    b = Board.objects.get(id=board_id)
    b.reply_set.create(
        comment=request.POST["comment"], rep_date=timezone.now())
    return HttpResponseRedirect(reverse("youareright:detail", args=(board_id,)))


# 해시태그 페이지
def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    boards = hashtag.board_set.order_by('-pk')
    return render(request, 'hashtag.html', {'hashtag': hashtag, 'boards': boards})