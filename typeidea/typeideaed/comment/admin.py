from django.contrib import admin
from .models import Comment
from typeideaed.custom_site import custom_site

# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['target', 'content', 'nickname', 'website', 'email', 'status', 'created_time',]


