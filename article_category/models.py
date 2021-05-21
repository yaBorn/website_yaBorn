# Create your models here.


from django.db import models
from django.utils import timezone

# 种类 ->文章 一对多
# 标签<->文章 多对多


# 文章种类
class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
