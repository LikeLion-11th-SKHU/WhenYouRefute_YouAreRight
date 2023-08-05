from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Board, Reply


def main(request):
    return render(request, "main.html")


def board(request):
    all_boards = Board.objects.all().order_by("-pub_date")
    return render(
        request, "board.html", {"title": "Board List", "board_list": all_boards}
    )


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, "detail.html", {"board": board})


def write(request):
    return render(request, "write.html")


def write_board(request):
    b = Board(
        title=request.POST["title"],
        content=request.POST["detail"],
        author="jun",
        pub_date=timezone.now(),
    )
    b.save()
    return HttpResponseRedirect(reverse("youareright:board"))


def create_reply(request, board_id):
    b = Board.objects.get(id=board_id)
    b.reply_set.create(comment=request.POST["comment"], rep_date=timezone.now())
    return HttpResponseRedirect(reverse("youareright:detail", args=(board_id,)))