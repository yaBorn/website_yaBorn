from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.http import JsonResponse
from article.models import Article

# DRF 序列化
from article.serializers import ArticleListSerializer
from article.serializers import ArticleDetailSerializer

# APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# 通用视图
from rest_framework import mixins
from rest_framework import generics

"""
# 对数据的增删改查是几乎每个项目的通用操作
# 通过 DRF 提供的 Mixin 类直接集成对应的功能。
# 提供了对文章详情的获取、修改、删除的 3 个方法
# 以及 1 个用于获取单个文章 model 的辅助方法
class ArticleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    #文章详情视图
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""


# 使用 Mixin 已经足够简单了，但我们还可以让它更简单：
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class article_list(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

"""
# @api_view 装饰器允许视图接收 GET 、POST 请求
# 以及提供如 405 Method Not Allowed 等默认实现
# 以便在不同的请求下进行正确的响应。
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
        # Response _Django 原生响应体扩展
        # 根据内容协商来确定返回给客户端的正确内容类型

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""