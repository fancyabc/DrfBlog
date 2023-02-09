
from rest_framework import generics
from rest_framework import mixins

from utils.permissions import IsAdminUserOrReadOnly

from article.models import Article
from article.serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleList(generics.ListCreateAPIView):

    permission_classes = [IsAdminUserOrReadOnly]  # 在此添加权限控制

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """文章详情视图"""

    permission_classes = [IsAdminUserOrReadOnly]  # 在此添加权限控制

    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
