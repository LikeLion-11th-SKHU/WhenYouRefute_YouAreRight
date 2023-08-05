from django.urls import path

from . import views

app_name = "youareright"
urlpatterns = [
    path("", views.board, name="board"),
    path("<int:board_id>/", views.detail, name="detail"),
    path("write/", views.write, name="write"),
    path("write/write_board/", views.write_board, name="write_board"),
    path("<int:board_id>/create_reply/", views.create_reply, name="create_reply"),
]
