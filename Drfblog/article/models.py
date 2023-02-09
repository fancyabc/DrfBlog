from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    """博客文章模型"""

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', null=True)   # 添加外键

    def __str__(self):
        return self.title
