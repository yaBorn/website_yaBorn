from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from article.models import Article
from django.contrib.auth.models import User


# 评论模型
class Comment(models.Model):
    # 作者 作者/评论->1/n
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    # 所属文章 文章/评论->1/n
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    content = models.TextField()  # 评论内容
    created = models.DateTimeField(default=timezone.now)  # 评论时间

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:20]
