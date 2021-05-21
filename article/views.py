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


# 提供了对文章详情的获取、修改、删除的 3 个方法
# 以及 1 个用于获取单个文章 model 的辅助方法
class ArticleDetail(APIView):
    """文章详情视图"""

    def get_object(self, pk):
        """获取单个文章对象"""
        try:
            # pk 即主键，默认状态下就是 id
            return Article.objects.get(pk=pk)
        except:
            raise Http404

    # DRF 类视图与传统 Django 的区别
    # .get() 、 .put() 多了将对象序列化/反序列化的步骤
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        # 返回 Json 数据
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data)
        # 验证提交的数据是否合法
        # 不合法则返回400
        if serializer.is_valid():
            # 序列化器将持有的数据反序列化后，
            # 保存到数据库中
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        # 删除成功后返回204
        return Response(status=status.HTTP_204_NO_CONTENT)


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
