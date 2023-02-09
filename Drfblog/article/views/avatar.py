from rest_framework import viewsets

from utils.permissions import IsAdminUserOrReadOnly

from article.models import Avatar
from article.serializers.avatar import AvatarSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]
