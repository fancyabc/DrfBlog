from rest_framework import viewsets

from utils.permissions import IsAdminUserOrReadOnly
from article.models import Tag
from article.serializers.tag import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None
