# @Time      : 2022/11/26  上午11:22
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : apis.py
# @Software  : PyCharm

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category, Tag
from .serializers import PostSerializer, PostDetailSerializer, \
                        CategorySerializer, TagSerializer,CategoryDetailSerializer, TagDetailSerializer

# @api_view() # api_view() 是把View 转换成API View 的装饰器
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts, many=True)
#     return Response(post_serializers.data)
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    # def filter_queryset(self, queryset):
    #     category_id = self.request.query_params.get('category')
    #     print('qq', self.request.query_params)
    #     if category_id:
    #         queryset = queryset.filter(category_id=category_id)
    #     return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)

class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super().retrieve(request, *args, **kwargs)






