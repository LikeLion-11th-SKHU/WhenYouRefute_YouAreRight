from django.contrib import admin
from django.urls import path
import youareright.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", youareright.views.index, name="index"),
    path("create/", youareright.views.create, name="create"),
    path("read/", youareright.views.read, name="read"),
    path("detail/<str:title>", youareright.views.detail, name="detail"),
    path("update/<str:title>", youareright.views.update, name="update"),
    path("delete/<str:title>", youareright.views.delete, name="delete"),
]
