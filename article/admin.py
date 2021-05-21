from django.contrib import admin

# Register your models here.
from django.contrib import admin

# 别忘了导入Article
from .models import Article

# 注册Article_Model到admin中
admin.site.register(Article)