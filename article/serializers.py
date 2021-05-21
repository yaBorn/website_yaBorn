# 前后端分离_序列化器_把 Python 对象转换为 JSON

from rest_framework import serializers
from article.models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]
