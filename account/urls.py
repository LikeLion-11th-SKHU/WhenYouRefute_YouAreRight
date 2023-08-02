from django.urls import path
from account import views
# static과 media 불러오기 위한 import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)