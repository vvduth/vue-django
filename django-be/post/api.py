from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse

from account.models import User
from account.serializers import UserSerializer
from .serializers import PostSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .form import  PostForm
from .models import Post
# Create your views here.

@api_view(['GET'])
def post_list(request):
    """
    View to list all posts.
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False,)

@api_view(['POST'])
def post_create(request):
    """
    View to create a new post.
    """
    data = request.data
    form = PostForm(data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        serializer = PostSerializer(post)
        return JsonResponse(serializer.data,safe=False ,status=201)
    else:
        return JsonResponse(form.errors, status=400)


@api_view(['GET'])
def post_list_by_user(request, id):
    """
    View to list all posts by a specific user.
    """
    user = User.objects.get(id=id)
    posts = Post.objects.filter(created_by_id=id)
    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    return JsonResponse({'posts': post_serializer.data ,
                         'user': user_serializer.data}, safe=False)

