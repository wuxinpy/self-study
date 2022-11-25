# @Time      : 2022/11/20  下午4:49
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path

from . import views

app_name = 'comment'
urlpatterns = [
    path('comment/', views.CommentView.as_view(), name='comment'),
]