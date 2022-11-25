# @Time      : 2022/11/20  下午4:49
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.post_list, name='index'),
    # path('category/<int:category_id>/', views.post_list, name='category'),
    # path('tag/<int:tag_id>/', views.post_list, name='tag'),
    # path('post/<int:post_id>.html', views.post_detail, name='detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', views.CategoryView.as_view(), name='category'),
    path('tag/<int:tag_id>/', views.TagView.as_view(), name='tag'),
    path('post/<int:post_id>.html', views.PostDetailView.as_view(), name='detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('author/<int:owner_id>', views.AuthorView.as_view(), name='author'),
]