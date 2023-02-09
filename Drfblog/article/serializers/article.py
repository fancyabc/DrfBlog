
from rest_framework import serializers
from article.models import Article

from .user_info import UserDescSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    """文章列表序列化器"""

    author = UserDescSerializer(read_only=True)     # 只读参数

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
            'author',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    """文章详情序列化器"""
    class Meta:
        model = Article
        fields = '__all__'  # 使用所有字段
