
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from utils.permissions import IsAdminUserOrReadOnly

from article.models import Article

from article.serializers.article import ArticleSerializer, ArticleDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        """在创建文章前，提供了视图集无法自行推断的用户外键字段"""
        serializer.save(author=self.request.user)   # 从Request中提取用户信息，将额外信息保存

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
