from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.http import JsonResponse
from article.models import Article
# 这个 ArticleListSerializer 暂时还没有
from article.serializers import ArticleListSerializer


# 视图函数
def article_list(request):
    # 取出所有文章的 QuerySet；
    articles = Article.objects.all()
    # 根据 QuerySet 数据，创建一个序列化器；
    serializer = ArticleListSerializer(articles, many=True)
    # 将序列化后的数据以 Json 的形式返回。
    return JsonResponse(serializer.data, safe=False)