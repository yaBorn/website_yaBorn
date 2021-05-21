# 前后端分离_序列化器_把 Python 对象转换为 JSON

from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer


# 简化序列化器_使用ModelSerializer
# 文章列表接口
class ArticleListSerializer(serializers.ModelSerializer):
    # 用户信息，嵌套序列化器
    author = UserDescSerializer(read_only=True)
    # json中直接提供超链接地址
    url = serializers.HyperlinkedIdentityField(view_name="article:detail")
    # 这里的name为urls的name母urls中app对应的namespace

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
            'created',
            'author',
        ]


# 文章详情接口
class ArticleDetailSerializer(serializers.ModelSerializer):
    # 嵌套用户信息
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段
