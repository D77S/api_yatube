#  from django.shortcuts import render
from posts.models import Post, Group, Comment
from posts.serializers import (PostSerializer,
                               CommentSerializer,
                               GroupSerializer
                               )

from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    # Наследовались специально от ReadOnly,
    # чтобы через api нельзя было создать новую группу.
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        new_queryset = Comment.objects.filter(
            author_id=self.kwargs.get("post_id")
        )
        return new_queryset
