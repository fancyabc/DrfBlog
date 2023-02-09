
from rest_framework import viewsets

from utils.permissions import IsAdminUserOrReadOnly

from article.models import Article

from article.serializers.article import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        """在创建文章前，提供了视图集无法自行推断的用户外键字段"""
        serializer.save(author=self.request.user)   # 从Request中提取用户信息，将额外信息保存


# class ArticleList(generics.ListCreateAPIView):
#
#     permission_classes = [IsAdminUserOrReadOnly]  # 在此添加权限控制
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)   # 从Request中提取用户信息，将额外信息保存
#
#
# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """文章详情视图"""
#
#     permission_classes = [IsAdminUserOrReadOnly]  # 在此添加权限控制
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

