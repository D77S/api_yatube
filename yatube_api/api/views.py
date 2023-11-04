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
        '''Получает все комменты к одному конкретному посту.
        '''
        # new_queryset = Comment.objects.filter(
        #     author_id=self.kwargs.get("post_id")
        # )
        new_queryset = Comment.objects.select_related('author').filter(author_id=self.kwargs.get("post_id"))
        return new_queryset

    def perform_create(self, serializer):
        # создания комента к нужному посту.
        # Срабатывает ТОЛЬКО на пост-запрос.
        print(self.post_id)
        serializer.save(author=self.request.user,
                        post=self.request.post_id,
                        )
        # print ('post_id=', self.post_id, ', pk=', self.pk)
        # return super().perform_create(serializer)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(instance)
