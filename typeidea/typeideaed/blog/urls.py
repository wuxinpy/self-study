# @Time      : 2022/11/20  下午4:49
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : urls.py
# @Software  : PyCharm
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from .apis import PostViewSet, CategoryViewSet, TagViewSet


router = DefaultRouter()
router.register('post', PostViewSet, basename='api-post')
router.register('category', CategoryViewSet, basename='api-category')
router.register('tag', TagViewSet, basename='api-tag')

app_name = 'blog'

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
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

    # path('api/post/', post_list, name='post-list'),
    path('api/', include(router.urls)),

    # path('api/docs/', include_docs_urls(title='typeidea apis'))
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]