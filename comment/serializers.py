# comment/serializers.py

from rest_framework import serializers

from comment.models import Comment
from user_info.serializers import UserDescSerializer


# 子评论接口
class CommentParentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')  # url超链
    author = UserDescSerializer(read_only=True)  # 嵌套序列化器 作者

    class Meta:
        model = Comment
        # 定义不需要的字段 父评论只需要超链和作者
        exclude = [
            'parent',
            'article'
        ]


# 评论接口
# 评论序列化器
class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')  # url超链
    author = UserDescSerializer(read_only=True)  # 嵌套序列化器 作者

    # 该评论所属文章
    # 文章不是视图集 按照根urls_文章urls设定
    article = serializers.HyperlinkedRelatedField(view_name='article:detail', read_only=True)
    article_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)

    # 该评论所属父评论
    parent = CommentParentSerializer(read_only=True)
    parent_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # 该评论更新时忽略父评论 只有创建时才能指定父评论
    def update(self, instance, validated_data):
        validated_data.pop('parent_id', None)
        return super().update(instance, validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'created': {
                'read_only': True
            }
        }

