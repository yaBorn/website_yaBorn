# 权限控制
from rest_framework import permissions

# 管理员修改 其他用户只读权限
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminUserOrReadOnly(BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """
    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD, OPTIONS 请求
        if request.method in SAFE_METHODS:
            return True
        # 仅管理员可进行其他操作
        return request.user.is_superuser


class IsOwnerOrReadOnly(BasePermission):
    """
    仅本人可进行修改
    所有人可查看
    """
    message = 'You must be the owner to update.'

    # 检查用户登录状态
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    # 验证作者和当前登录用户是用一个人
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
