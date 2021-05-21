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
# from article.serializers import ArticleListSerializer, ArticleDetailSerializer
from rest_framework.permissions import IsAdminUser
from article.permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets
from article.serializers import ArticleSerializer


# 视图集
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
