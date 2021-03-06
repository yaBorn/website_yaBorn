# 引入path
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    # 文章列表
    # 之前是函数视图，现在是类视图
    # path('article-list/', views.article_list, name='article_list'),
    path('article-list/', views.ArticleListView.as_view(), name='list'),

    # 文章详情
    # path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-detail/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
]
