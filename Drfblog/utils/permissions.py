
from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """
    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD, OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 仅管理员可进行其他操作
        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    """自定义一个所有人都可查看、仅本人可更改的权限"""

    message = 'You must be the owner to update.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsSelfOrReadOnly(permissions.BasePermission):
    """确保非安全方法只能由本人操作"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user
