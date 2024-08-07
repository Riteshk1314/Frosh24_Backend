from django.urls import path
from .views import LoginView,ForgotPassword
# from .views import userinfo
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgotpass'),
    
    # path('user/', views.userinfo, name='userinfo'),
]
