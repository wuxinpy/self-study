# @Time      : 2022/11/29  下午10:06
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path
from .views import *

app_name = 'commodity'

urlpatterns = [
    path('.html', commodityView, name='commodity'),
    path('/detail.<int:id>.html', detailView, name='detail'),
    path('/collect.html', collectView, name='collect'),

    # path('.html', CommodityView.as_view(), name='commodity'),
]