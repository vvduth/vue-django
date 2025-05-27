from django.http import JsonResponse
from account.models import User
from post.models import Post
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.serializers import UserSerializer
from post.serializers import PostSerializer


@api_view(['POST'])
def search(request):
    """
    Handle search requests.
    """
    query = request.data.get('query', '')

    users = User.objects.filter(name__icontains=query)
    user_serializer = UserSerializer(users, many=True)

    posts = Post.objects.filter(body__icontains=query)
    post_serializer = PostSerializer(posts, many=True)

    return JsonResponse({'users':user_serializer.data,
                         'posts': post_serializer.data}, safe=False, status=200)