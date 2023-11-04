from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from posts.serializers import (CommentSerializer, GroupSerializer,
                               PostSerializer)
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        '''Перегружает метод вьюсета по созданию объекта.
        При создании поста нам надо, чтобы
        id автора камента брался именно из реквеста
        (даже если какой-то и пришел в словаре api, мы ему не верим).
        '''
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        '''Перегружает метод вьюсета по обновлению объекта,
        хоть частичному хоть полному.
        Вызывает родительский (неперегруженный) метод, только если
        совпадает автор обновляемого объекта и залогиненный пользователь.
        '''
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        '''Перегружает метод вьюсета по удалению объекта.
        Вызывает родительский (неперегруженный) метод, только если
        совпадает автор удаляемого объекта и залогиненный пользователь.
        '''
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для групп постов.
    Наследовались специально от ReadOnly,
    чтобы через api нельзя было создать новую группу.
    А только через админку можно было бы.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        '''Перегружает кверисет таким образом,
        чтобы он содержал не вообще все каменты,
        а только каменты к одному конкретному посту.
        Номер поста через кварг получаем из урла.
        '''
        print(self.kwargs)
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        '''Перегружает метод вьюсета по созданию объекта.
        При создании камента нам надо, чтобы:
        - id автора камента брался именно из реквеста
        (даже если какой-то и пришел в словаре api, мы ему не верим);
        - номер пост, к которому создаем камент, берем из урла по регулярке и
        вытаскиваем сей объект поста из базы постов.
        '''
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        '''Перегружает метод вьюсета по обновлению объекта,
        хоть частичному хоть полному.
        Вызывает родительский (неперегруженный) метод, только если
        совпадает автор обновляемого объекта и залогиненный пользователь.
        '''
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        '''Перегружает метод вьюсета по удалению объекта.
        Вызывает родительский (неперегруженный) метод, только если
        совпадает автор удаляемого объекта и залогиненный пользователь.
        '''
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(instance)
