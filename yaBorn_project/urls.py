"""yaBorn_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
# 不同模块同名Views，直接导入则冲突
from media.views import PhotoViewSet
from comment.views import CommentViewSet


# 使用视图集的 views视图 ,使用 router 自动处理视图的url
# 因为视图集自带了list instance等行为
#   直接在根url注册即可
# 文章列表/详情 种类列表/详情 使用generics.API视图
#   自己写了列表/详情，在对应模块urls下写分级url
router = routers.DefaultRouter()
router.register(r'photo', PhotoViewSet)
router.register(r'comment', CommentViewSet)

# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),

    # 添加 DRF 登录视图，以便 DRF 自动为可视化接口页面生成用户登录入口：
    path('api-auth/', include('rest_framework.urls')),

    # 配置自定app的url
    path('article/', include('article.urls', namespace='article')),
    path('category/', include('article_category.urls', namespace='category')),

    # drf 自动注册路由_视图集
    # media资源储存在 media/...
    # api/... 管理视图集行为 list Instance 等
    path('api/', include(router.urls)),
]

# 资源文件路由注册
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    后台管理：http://127.0.0.1:8000/admin/ 
    文章列表：http://127.0.0.1:8000/article/article-list/
    种类列表：http://127.0.0.1:8000/category/category-list/
    标签列表：http://127.0.0.1:8000/category/tag-list/
    视图集根目录：http://127.0.0.1:8000/api/
        视图集使用：
            图片 photo
            评论 comment
    图片资源：http://127.0.0.1:8000/media/photo
"""
