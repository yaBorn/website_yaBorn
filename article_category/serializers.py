# 序列化器
from rest_framework import serializers

from article.models import Article
from article_category.models import Category


# 类别列表接口
class CategoryListSerializer(serializers.ModelSerializer):
    """分类列表序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="article_category:detail")

    class Meta:
        model = Category
        fields = '__all__'


# 文章url接口
# 嵌套于类别详情序列化器
class ArticleUrlSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article:detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


# 类别详情接口
class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情序列化器"""
    articles = ArticleUrlSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]
