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


# 标签接口
# 子类： 标签_列表/详情
class TagBaseSerializer(serializers.ModelSerializer):
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


# 标签列表接口
class TagListSerializer(TagBaseSerializer):
    """标签列表"""
    url = serializers.HyperlinkedIdentityField(view_name="article_category:tag_detail")

    class Meta:
        model = Tag
        fields = [
            'text',
            'url',
        ]


# 标签详情接口
class TagDetailSerializer(TagBaseSerializer):
    """标签详情"""
    articles = ArticleUrlSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = [
            'text',
            'articles',
        ]





