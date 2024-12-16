"""API Endpoints"""

from django.http import JsonResponse  # type: ignore
from users.models import User
from users.managers import UserManager

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

####################################################################################################
# Index
####################################################################################################


def index(request):
    """Root views for the API Server."""
    if request.method == "GET":
        return JsonResponse(
            {"status": "OK", "message": "API is running.", "version": "1.0.0"},
            status=200,
        )

    return JsonResponse(
        {"status": "ERROR", "message": "Invalid request method."}, status=405
    )


####################################################################################################
# Users
####################################################################################################


@api_view(["GET"])
def get_users(request) -> Response:
    """Get all users."""
    return Response(UserSerializer(User.objects.all(), many=True).data)


@api_view(["GET"])
def get_user(request, id: int) -> Response:
    """Get user by ID."""
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(
            {"status": "ERROR", "message": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response(UserSerializer(user).data)


@api_view(["POST"])
def create_user(request):
    """Create a new user.

    POST Parameters:
    - email: str (unique - IIMK email)
    - first_name: str
    - last_name: str
    - password: str

    Returns:
    - user: json
    """
    user_data = UserSerializer(data=request.data)
    if user_data.is_valid():
        # create user
        user = user_data.save()
        user.set_password(user.password)
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_user(request, id: int):  # TODO: Rewrite this function to use partial updates
    """Update a user.

    POST Parameters:
    - id: int (mandatory)
    - first_name: str (optional)
    - last_name: str (optional)
    - password: str (optional)

    Returns:
    - user: json
    """
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(
            {"status": "ERROR", "message": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        if "first_name" in request.data:
            user.first_name = request.data["first_name"]
        if "last_name" in request.data:
            user.last_name = request.data["last_name"]
        if "password" in request.data:
            user.set_password(user.password)
        user.save()

        if "password" not in request.data:
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(
            {"status": "OK", "message": "Password changed successfully."},
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        return Response(
            {"status": "ERROR", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["DELETE"])
def delete_user(request, id: int):
    """Delete a user."""
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(
            {"status": "ERROR", "message": "User not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    user.delete()
    return Response(
        {"status": "OK", "message": "User deleted successfully."},
        status=status.HTTP_204_NO_CONTENT,
    )
