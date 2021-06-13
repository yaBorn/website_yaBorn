# Create your views here.
from rest_framework import filters
from rest_framework import generics
from yaBorn_project.permissions import IsAdminUserOrReadOnly
from article_category.models import Category, Tag
from article_category.serializers import CategoryListSerializer, CategoryDetailSerializer, TagListSerializer, \
    TagDetailSerializer


# 分类列表
class CategoryListView(generics.ListCreateAPIView):
    """分类列表视图"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # 模糊搜索 搜索后端Django的SearchFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    # 一次性返回所有信息 不受翻页影响
    pagination_class = None


# 分类详情
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """分类详情视图"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# 标签列表
class TagListView(generics.ListCreateAPIView):
    """标签列表视图"""
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # 模糊搜索 搜索后端Django的SearchFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    # 一次性返回所有信息 不受翻页影响
    pagination_class = None


# 标签详情
class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """标签详情视图"""
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]