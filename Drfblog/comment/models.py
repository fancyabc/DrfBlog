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

    # 多级评论，让评论模型和自身相关联，使其可以有一个父级。
    comment_p = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='comment_s'
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:20]
