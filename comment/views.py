from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer
from yaBorn_project.permissions import IsOwnerOrReadOnly


# 评论 视图集
# 自带 list instance等
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)