from rest_framework import serializers

from posts.models import Post  # , Group, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
