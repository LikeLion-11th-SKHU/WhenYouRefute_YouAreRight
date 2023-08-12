from django.urls import path

from . import views

app_name = "youareright"
urlpatterns = [
    path("", views.board, name="board"),
    path("<int:board_id>/", views.detail, name="detail"),
    path("write/", views.write, name="write"),
    path("<int:board_id>/create_reply/", views.create_reply, name="create_reply"),
    path('<int:hashtag_pk>/hashtag/', views.hashtag, name='hashtag'),
    path("<int:board_id>/update/", views.update, name="update"),
]
