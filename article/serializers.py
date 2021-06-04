# 前后端分离_序列化器_把 Python 对象转换为 JSON
# 简化序列化器_使用ModelSerializer
from rest_framework import serializers
from article.models import Article
from article_category.models import Category, Tag
from comment.serializers import CommentSerializer
from media.models import Photo
from media.serializer import PhotoSerializer
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


# 文章父类
# 被继承子类: 文章_列表/详情
class ArticleBaseSerializer(serializers.ModelSerializer):
    # vue-router 前端路由 使用文章id作为动态地址
    id = serializers.IntegerField(read_only=True)

    # 用户信息，嵌套序列化器
    author = UserDescSerializer(read_only=True)
    # 这里的name为urls的name母urls中app对应的namespace
    # 分类信息，嵌套序列化器
    category = CategorySerializer(read_only=True)
    # 分类id
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    # 标签 字段
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )
    # 图片字段
    photo = PhotoSerializer(read_only=True)
    photo_id = serializers.IntegerField(
        write_only=True,
        allow_null=True,
        required=False
    )

    # 验证图片 id 是否存在 否则返回错误
    def validate_photo_id(self, value):
        if not Photo.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Photo with id {} not exists.".format(value))
        return value

    # category_id 字段的验证器
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exists.".format(value))
        return value

    # 覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')
        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)
        return super().to_internal_value(data)


# 文章列表接口
class ArticleListSerializer(ArticleBaseSerializer):
    """文章列表序列化器"""
    # json中直接提供超链接地址
    url = serializers.HyperlinkedIdentityField(view_name="article:detail")

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
            'photo',
        ]


# 文章详情接口
class ArticleDetailSerializer(ArticleBaseSerializer):
    """文章详情序列化器"""
    # markdown渲染后的正文
    body_html = serializers.SerializerMethodField()
    # markdown渲染后的目录
    toc_html = serializers.SerializerMethodField()
    #   后端存储body，前端需要md化后的字符，后端直接将md化的字符给前端读取
    #   SMF为只读字段，调用附加方法获取值
    #   即body_html会自动调用getBH方法，返回结果作为序列化数据
    # 文章详情_评论 嵌套序列化器
    id = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def get_body_html(self, obj):
        # obj为序列化器获取的model实例，即文章对象了
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段
