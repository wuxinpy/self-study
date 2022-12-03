# @Time      : 2022/11/29  下午10:06
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm

from django.urls import path
from .views import *

app_name = 'index'

urlpatterns = [
    path('', indexView, name='index'),
    # path('', IndexView.as_view(), name='index'),
]
