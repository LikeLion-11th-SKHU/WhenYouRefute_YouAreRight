from django.urls import path

from . import views

app_name = "youareright"
urlpatterns = [
    path("", views.board, name="board"),
    path("<int:board_id>/", views.detail, name="detail"),
    path("write/", views.write, name="write"),
    path("write/write_board/", views.write_board, name="write_board"),
    path("<int:board_id>/create_reply/", views.create_reply, name="create_reply"),
    path("<int:board_id>/edit/", views.edit, name="edit"),
    path("<int:board_id>/update/", views.update, name="update"),
    path("<int:board_id>/delete/", views.delete, name="delete"),
]
