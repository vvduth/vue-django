from django.http import JsonResponse
from account.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.serializers import UserSerializer


@api_view(['POST'])
def search(request):
    """
    Handle search requests.
    """
    query = request.data.get('query', '')

    users = User.objects.filter(name__icontains=query)
    user_serializer = UserSerializer(users, many=True)

    return JsonResponse(user_serializer.data, safe=False, status=200)