from django.contrib import admin
from django.urls import path
import youareright.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", youareright.views.main, name="main"),
    path("create/", youareright.views.create, name="create"),
    path("board/", youareright.views.board, name="board"),
    path("detail/<int:id>", youareright.views.detail, name="detail"),
    path("update/<int:id>", youareright.views.update, name="update"),
    path("delete/<int:id>", youareright.views.delete, name="delete"),
    path('<int:hashtag_pk>/hashtag/', youareright.views.hashtag, name='hashtag'),
] 
