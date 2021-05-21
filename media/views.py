from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from media.models import Photo
from media.serializer import PhotoSerializer
from yaBorn_project.permissions import IsAdminUserOrReadOnly


# 图像 视图集
# 自带 list instance等
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAdminUserOrReadOnly]
