# 前后端分离_序列化器_把 Python 对象转换为 JSON

from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer


# 简化序列化器_使用ModelSerializer
# 文章列表接口
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


# 文章详情接口
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段
