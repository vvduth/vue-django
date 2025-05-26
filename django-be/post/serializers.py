from account.serializers import UserSerializer
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """

    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'body', 'created_at_formatted', 'created_by']