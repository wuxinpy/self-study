from django.contrib import admin
from .models import *

admin.site.site_title = '我的音乐后台管理系统'
admin.site.site_header = '我的音乐'


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'singer', 'album', 'languages', 'release', 'img', 'lyrics', 'file']
    search_fields = ['name', 'singer', 'album', 'languages']
    list_filter = ['singer', 'album', 'languages']
    ordering = ['id']
    save_on_top = True
    save_as = True

@admin.register(Dynamic)
class DynamicAdmin(admin.ModelAdmin):
    list_display = ['id', 'song', 'search', 'plays', 'download']
    search_fields = ['song']
    list_filter = ['plays', 'search', 'download']
    ordering = ['id']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'song', 'date']
    search_fields = ['user', 'song', 'date']
    list_filter = ['song', 'date']
    ordering = ['id']

