# 序列化器
from rest_framework import serializers
from article.models import Article
from article_category.models import Category, Tag


# 文章url接口
# 嵌套于序列化器: 类别_详情 标签_详情
class ArticleUrlSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article:detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
            'created',
            'updated',
        ]


# 类别列表接口
class CategoryListSerializer(serializers.ModelSerializer):
    """分类列表"""
    url = serializers.HyperlinkedIdentityField(view_name="article_category:detail")

    class Meta:
        model = Category
        fields = '__all__'


# 类别详情接口
class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleUrlSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]


# 标签列表接口
class TagListSerializer(serializers.ModelSerializer):
    """标签列表"""
    url = serializers.HyperlinkedIdentityField(view_name="article_category:tag_detail")

    class Meta:
        model = Tag
        fields = [
            'text',
            'url',
        ]


# 标签详情接口
class TagDetailSerializer(serializers.ModelSerializer ):
    """标签详情"""
    articles = ArticleUrlSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = [
            'text',
            'articles',
        ]





