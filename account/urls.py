from django.urls import path
from account import views
# static과 media 불러오기 위한 import
from django.conf import settings
from django.conf.urls.static import static
import account.views

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)