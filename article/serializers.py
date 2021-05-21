# 前后端分离_序列化器_把 Python 对象转换为 JSON

from rest_framework import serializers
from article.models import Article


# 简化序列化器_使用ModelSerializer
# 文章列表接口
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]


# 文章详情接口
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段
