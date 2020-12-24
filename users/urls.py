"""定义users的URL模式"""
from django.urls import path
from .controller import users

app_name='users';
urlpatterns = [
    # 登陆
    path('login', users.login, name='login'),
]