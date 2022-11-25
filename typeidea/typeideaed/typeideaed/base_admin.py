# @Time      : 2022/11/20  下午4:17
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : base_admin.py
# @Software  : PyCharm

from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1、补全分类、标签、文章、友链、侧边栏的'owner'字段
    2、过滤当前用户数据
    """

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)