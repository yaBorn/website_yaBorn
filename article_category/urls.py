# 引入path
from django.urls import path, include
from . import views
from rest_framework import routers

# 正在部署的应用的名称
app_name = 'article_category'

urlpatterns = [
    # 类别 列表
    path('category-list/', views.CategoryListView.as_view(), name='list'),
    # 类别 详情
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view(), name='detail'),
    # 标签 列表
    path('tag-list/', views.TagListView.as_view(), name='tag_list'),
    # 标签 详情
    path('tag-detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),

]

