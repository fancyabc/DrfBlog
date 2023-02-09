from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from article.models import Article


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:20]
