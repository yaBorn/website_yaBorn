from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User  # 导入内建的User模型。
from django.utils import timezone  # timezone 用于处理时间相关事务。


# 博客文章数据模型
class Article(models.Model):
    # 文章作者
    # ForeignKey 外键 文章作者1对多
    # 参数 on_delete 指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    # models.CharField 字符串字段，保存较短的字符串
    title = models.CharField(max_length=100)

    # 文章正文
    # 大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间
    # 参数 default=timezone.now 创建数据时默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章修改时间
    # 参数 auto_now=True 数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 模型返回的数据排列顺序
        # '-created' 表明数据倒序排列
        ordering = ('-created',)

    # 函数 __str__ 调用对象的 str() 方法时返回值内容
    def __str__(self):
        # return self.title 文章标题返回
        return self.title
