# @Time      : 2022/11/29  下午10:06
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path
from .views import *

app_name = 'shopper'
urlpatterns = [
    path('.html', shopperView, name='shopper'),
    path('/login.html', loginView, name='login'),
    path('/logout.html', logoutView, name='logout'),
    path('/shopcart.html', shopCartView, name='shopcart'),
    path('/delete.html', deleteAPI, name='delete'),
]