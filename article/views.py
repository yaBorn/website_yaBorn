# Create your views here.

# 导入 HttpResponse 模块
from rest_framework import generics
from article.models import Article
from article.serializers import ArticleListSerializer, ArticleDetailSerializer
from yaBorn_project.permissions import IsAdminUserOrReadOnly
from rest_framework import filters


# 文章列表
# 类视图+APIView_文章列表
class ArticleListView(generics.ListCreateAPIView):
    """文章列表视图"""
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # 只允许管理员发布文章
    permission_classes = [IsAdminUserOrReadOnly]
    # 模糊搜索 搜索后端Django的SearchFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    # 使文章发表时对应一位作者(防止空和伪造用户id)
    # 序列化数据前调用 保存额外的数据
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# 文章详情
# 类视图+简化_文章详情_增删改查的函数简化掉
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """文章详情视图"""
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]


