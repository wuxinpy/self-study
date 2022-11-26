from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .models import Category, Tag, Post
from .adminforms import PostAdminForm
from typeideaed.custom_site import custom_site
from typeideaed.base_admin import BaseOwnerAdmin

# Register your models here.

class PostInLine(admin.TabularInline):
    fields = ['title', 'desc', 'owner']
    extra = 1
    model = Post


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器，只展示当前用户创建的分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'is_nav', 'created_time', 'post_count', 'owner']
    fields = ['name', 'status', 'is_nav']
    inlines = [PostInLine, ]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time', 'post_count', 'owner']
    fields = ['name', 'status']

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = ['title', 'category', 'status', 'created_time', 'operator', 'owner', 'pv', 'uv']
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True


    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
                # 'content_ck',
                # 'content_md',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tag',),
        }),
    )


    filter_horizontal = ('tag',)

    def operator(self, obj):
        """自定义字段"""
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']