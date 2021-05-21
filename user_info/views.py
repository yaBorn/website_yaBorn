from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from user_info.serializers import UserRegisterSerializer
from yaBorn_project.permissions import IsSelfOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from user_info.serializers import UserDetailSerializer


# 用户 视图集
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # user模型 django已有模块
    serializer_class = UserRegisterSerializer
    lookup_field = 'username'  # 对应序列化器 UserRegisterSerializer 中的url解析

    # 权限管理
    def get_permissions(self):
        if self.request.method == 'POST':
            # POST请求 注册用户 允许所有人操作
            self.permission_classes = [AllowAny]
        else:
            # 其他请求 需要本人操作
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]
        return super().get_permissions()

    # 自定义动作
    # 用户详情 user/$ name/info
    @action(detail=True, methods=['get'])
    def info(self, request, username=None):
        queryset = User.objects.get(username=username)
        serializer = UserDetailSerializer(queryset, many=False)  # 使用详情序列化器
        return Response(serializer.data)

