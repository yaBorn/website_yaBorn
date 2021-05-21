from django.contrib import admin

# Register your models here.
from article_category.models import Category, Tag

admin.site.register(Category)
admin.site.register(Tag)
