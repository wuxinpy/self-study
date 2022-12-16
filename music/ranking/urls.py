# @Time      : 2022/12/14  下午9:19
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path
from .views import *

urlpatterns = [
    path('', rankingView, name='ranking'),
    # path('.list', RankingList.as_view(), name='rankingList'),
]