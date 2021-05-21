# 用户信息app序列化器

from django.contrib.auth.models import User
from rest_framework import serializers


# 文章关联用户时，将外键存入序列化数据
# 因此可以嵌套序列化数据，使得不只是显示作者id
# 用于文章列表中(article_views_articleList)，显示用户基本信息
class UserDescSerializer(serializers.ModelSerializer):
    """于文章列表中引用的嵌套序列化器"""
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'date_joined'
        ]
