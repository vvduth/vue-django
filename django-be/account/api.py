from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import  SignUpForm

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