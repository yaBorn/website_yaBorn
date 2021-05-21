from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.http import JsonResponse
from article.models import Article
# DRF 序列化
from article.serializers import ArticleListSerializer
# APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
