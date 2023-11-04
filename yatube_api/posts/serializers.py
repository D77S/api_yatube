from posts.models import Post, Group, Comment

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Post
        fields = 'id', 'text', 'pub_date', 'author', 'image', 'group', 'comments'
        read_only_fields = (
            'author',
            'group',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = 'id', 'author', 'post', 'text', 'created'
        read_only_fields = ('author', 'post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = (
            'author',
            'post',
            'created'
        )
