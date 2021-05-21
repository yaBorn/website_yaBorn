# 引入path
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# 正在部署的应用的名称
app_name = 'article_category'

urlpatterns = [
    # 文章类别 列表
    path('category-list/', views.CategoryListView.as_view(), name='list'),
    # 文章类别 详情
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view(), name='detail'),
]
