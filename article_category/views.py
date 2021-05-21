# Create your views here.


from rest_framework import generics
from article.permissions import IsAdminUserOrReadOnly
from article_category.models import Category
from article_category.serializers import CategoryListSerializer, CategoryDetailSerializer


# 分类列表
class CategoryListView(generics.ListCreateAPIView):
    """分类列表视图"""
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# 分类详情
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """文章详情视图"""
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]