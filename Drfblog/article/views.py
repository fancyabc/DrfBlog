
from rest_framework import generics

from article.models import Article
from article.serializers import ArticleListSerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
