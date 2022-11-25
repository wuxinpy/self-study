# @Time      : 2022/11/20  下午3:32
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : custom_site.py
# @Software  : PyCharm

from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea 管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')

