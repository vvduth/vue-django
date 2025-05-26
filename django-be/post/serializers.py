from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    class Meta:
        model = Post
        fields = ['id', 'body', 'created_at', 'created_by', 'attachments']
        read_only_fields = ['id', 'created_at', 'created_by']