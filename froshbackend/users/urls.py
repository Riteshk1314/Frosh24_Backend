from django.urls import path
from .views import LoginView
from .views import userinfo
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user/', userinfo.as_view(), name='userinfo'),
]
