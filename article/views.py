from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from article.models import Article
from article.serializers import ArticleListSerializer, ArticleDetailSerializer


# 文章列表
# 类视图+APIviewer_文章列表
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


# 文章详情
# 类视图+简化_文章详情_增删改查的函数简化掉
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
