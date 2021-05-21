# 前后端分离_序列化器_把 Python 对象转换为 JSON

from rest_framework import serializers
from article.models import Article
from article_category.models import Category
from user_info.serializers import UserDescSerializer
# 简化序列化器_使用ModelSerializer


# 文章类别接口
# 嵌套于文章列表/详情序列化器中
class CategorySerializer(serializers.ModelSerializer):
    """分类序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="article_category:detail")

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'url',
            'created',
        ]
        read_only_fields = ['created']


# 文章列表接口
class ArticleListSerializer(serializers.ModelSerializer):
    """文章列表序列化器"""
    # 用户信息，嵌套序列化器
    author = UserDescSerializer(read_only=True)
    # json中直接提供超链接地址
    url = serializers.HyperlinkedIdentityField(view_name="article:detail")
    # 这里的name为urls的name母urls中app对应的namespace
    # 分类信息，嵌套序列化器
    category = CategorySerializer(read_only=True)
    # 分类id
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # category_id 字段的验证器
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exists.".format(value))
        return value

    class Meta:
        model = Article
        fields = [
            'title',
            'url',
            'author',
            'created',
            'category',
            'category_id',
        ]


# 文章详情接口
class ArticleDetailSerializer(serializers.ModelSerializer):
    """文章详情序列化器"""
    # 嵌套用户信息
    author = UserDescSerializer(read_only=True)
    # 分类信息，嵌套序列化器
    category = CategorySerializer(read_only=True)
    # 分类id
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # category_id 字段的验证器
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exists.".format(value))
        return value

    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段



