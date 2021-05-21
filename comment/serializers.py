# comment/serializers.py

from rest_framework import serializers

from comment.models import Comment
from user_info.serializers import UserDescSerializer


# 评论接口
# 评论序列化器
class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')  # url超链
    author = UserDescSerializer(read_only=True)  # 嵌套序列化器 作者

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'created': {
                'read_only': True
            }
        }
