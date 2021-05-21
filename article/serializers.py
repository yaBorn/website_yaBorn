# 前后端分离_序列化器_把 Python 对象转换为 JSON
# 简化序列化器_使用ModelSerializer
from rest_framework import serializers
from article.models import Article
from article_category.models import Category, Tag
from user_info.serializers import UserDescSerializer


# 类别接口
# 嵌套于序列化器: 文章_列表/详情
class CategorySerializer(serializers.ModelSerializer):
    """分类序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="article_category:detail")

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'url',
        ]


# 标签接口
# 嵌套于序列器： 文章_列表/详情
class TagSerializer(serializers.ModelSerializer):
    """标签序列化器"""
    class Meta:
        model = Tag
        fields = '__all__'

    # 检查是否有重复text
    def check_tag_obj_exists(self, validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError('Tag with text {} exists.'.format(text))

    # 覆写create，检查text重复
    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    # 覆写update，检查text重复
    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)


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

    # 标签 字段
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )

    # 覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

    class Meta:
        model = Article
        fields = [
            'title',
            'url',
            'author',
            'created',
            'category',
            'category_id',
            'tags',
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

    # 标签 字段
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )

    # 覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段


