from django.db import models

# Create your models here.


# 图像模型
class Photo(models.Model):
    title = models.CharField(max_length=100)  # 标题
    describe = models.TextField()  # 补充描述
    content = models.ImageField(upload_to='photo/%Y%m%d')  # 图片字段
    # 保存在 res-media/photo/年月日/路径中
