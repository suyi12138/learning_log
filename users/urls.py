"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销登录
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册界面
    url(r'^register/$', views.register, name='register'),
]