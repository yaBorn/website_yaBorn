# 用户信息app序列化器

from django.contrib.auth.models import User
from rest_framework import serializers


# 用户嵌套序列化器
# 文章关联用户时，将外键存入序列化数据
# 因此嵌套序列化数据，使得不只是显示作者id
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


# 用户详情序列化器
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_name',
            'first_name',
            'email',
            'last_login',
            'date_joined'
        ]


# 用户管理序列化器
# 用户列表接口
class UserRegisterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')
    # lookup_field 指定解析超链字段，即用户详情接口地址表示为用户名而不是主键id

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'password',
            'is_superuser',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            # 判断当前用户是否为管理员
            'is_superuser': {'read_only': True},
        }

    # 创建用户时
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            # 更新时密码经过加密存入数据库
            instance.set_password(password)
        return super().update(instance, validated_data)
