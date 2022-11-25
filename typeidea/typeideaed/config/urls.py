# @Time      : 2022/11/20  下午4:49
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path

from . import views

app_name = 'config'
urlpatterns = [
    path('links/', views.LinkListView.as_view(), name='links'),
]