# Create your models here.

from django.db import models
from django.db import models
from django.contrib.auth.models import User  # 导入内建的User模型。
from django.utils import timezone  # timezone 用于处理时间相关事务。
from article_category.models import Category


# 博客文章数据模型
class Article(models.Model):
    # 文章分类 外键
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )

    # 文章作者 ForeignKey 外键
    author = models.ForeignKey(
        User,
        null=True,
        related_name='articles',
        on_delete=models.CASCADE,)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文
    body = models.TextField()

    # 文章创建时间
    created = models.DateTimeField(default=timezone.now)

    # 文章修改时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 模型返回的数据排列顺序 '-created' 表明数据倒序排列
        ordering = ('-created',)

    # 函数 __str__ 调用对象的 str() 方法时返回值内容
    def __str__(self):
        # return self.title 文章标题返回
        return self.title
