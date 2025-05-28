from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import  SignUpForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(['GET'])
def me(request):
    """
    Return the current user's information.
    """
    user = request.user
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
    }

    return JsonResponse(data, status=200)




@api_view(['POST'])
@authentication_classes([])  # No authentication required for signup
@permission_classes([])  # No permission required for signup
def signup(request):
    """
    Handle user signup.
    """
    # Here you would typically handle user creation logic
    # For now, we return a simple success message
    data = request.data
    message = ''
    form = SignUpForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    if form.is_valid():
        user = form.save()
        # send verification email
    else:
        return JsonResponse({"error": form.errors, "message": 'Error sign up'}, status=400)


    return JsonResponse({"message": "User signed up successfully!"}, status=201)

@api_view(['GET'])
def friends(request,pk):
    """
    Return the friends of a user.
    """
    friendship_requests  = []
    user = User.objects.get(pk=pk)

    if user == request.user:
        friendship_requests = FriendshipRequest.objects.filter(created_for=request.user, status=FriendshipRequest.SENT)
        friendship_requests = FriendshipRequestSerializer(friendship_requests, many=True).data
    user_friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(user_friends, many=True).data,
        'friendship_requests': friendship_requests
    }, safe=False, status=200)

@api_view(['POST'])
def send_friendship_request(request, pk):
    """
    Send a friendship request to another user.
    """
    print("Sending friendship request to user with ID:", pk)
    user = User.objects.get(pk=pk)
    friendship_request =  FriendshipRequest.objects.create(created_for=user, created_by=request.user)

    return JsonResponse({"message": "Friendship request sent successfully!"}, status=201)

@api_view(['POST'])
def handle_friendship_request(request, pk, action):
    """
    Handle friendship request actions (accept or reject).
    """
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship_request.status = action
    friendship_request.save()

    user.friends.add(request.user)
    user.friends_count += 1
    user.save()

    request_user = request.user
    request_user.friends.add(user)
    request_user.friends_count += 1
    request_user.save()


    return JsonResponse({"message": f"Friendship request {action} successfully!"}, status=200)