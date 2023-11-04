from posts.models import Post, Group, Comment

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    '''Класс сериализатора постов.'''
    # В поле автора хотим отдавать не id, а имя автора, поэтому
    # слегка переопределим поле author.
    # А по получении, хотим его игнорировать (read_only=True)
    # и брать из реквеста.
    author = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        # Перечень сериализируемых полей.
        # Можно было бы и просто __all__,
        # но нам надо добавить related поле comments.
        fields = ('id',
                  'text',
                  'pub_date',
                  'author',
                  'image',
                  'group',
                  'comments',
                  )
        read_only_fields = (
            'author',
            'group',
        )


class CommentSerializer(serializers.ModelSerializer):
    '''Класс сериализатора каментов к постам.'''
    # В поле автора хотим отдавать не id, а имя автора, поэтому
    # слегка переопределим поле author.
    # А по получении, хотим его игнорировать (read_only=True)
    # и брать из реквеста.
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = 'id', 'author', 'post', 'text', 'created'
        read_only_fields = ('author', 'post',)


class GroupSerializer(serializers.ModelSerializer):
    '''Класс сериализатора групп постов.'''
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = (
            'author',
            'post',
            'created'
        )
