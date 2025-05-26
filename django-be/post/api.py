from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Post
# Create your views here.

@api_view(['GET'])
def post_list(request):
    """
    View to list all posts.
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({ 'data': serializer.data })

