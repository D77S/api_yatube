#  from django.shortcuts import render

from rest_framework import viewsets
# from rest_framework.permissions import

from posts.models import Post, Group, Comment
from posts.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        pass
        #  if serializer.instance.author != self.request.user:
        #      raise PermissionDenied('Изменение чужого контента запрещено!')
        #  super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        pass
        #  if serializer.instance.author != self.request.user:
        #      raise PermissionDenied('Удаление чужого контента запрещено!')
        #  super(PostViewSet, self).perform_destroy(serializer)


class GroupViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        new_queryset = Comment.objects.filter(author_id=self.kwargs.get("post_id"))
        return new_queryset
