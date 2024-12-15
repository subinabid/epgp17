"""API Endpoints"""

from django.http import JsonResponse  # type: ignore
from django.contrib.auth.models import User  # type: ignore


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


def create_user(request):
    """Create a new user.

    POST Parameters:
    - email: str (unique - IIMK email)
    - first_name: str
    - last_name: str
    - password: str

    Returns:
    - user: dict
    """
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")

        # check if all parameters are present
        if not username or not first_name or not last_name or not password:
            return JsonResponse(
                {"status": "ERROR", "message": "Missing required parameters."},
                status=400,
            )

        # check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"status": "ERROR", "message": "User already exists."}, status=400
            )

        # check if email is valid
        if not username.endswith("@iimk.edu.in"):
            return JsonResponse(
                {"status": "ERROR", "message": "Invalid email. Must be IIMK email."},
                status=400,
            )

        # create user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        return JsonResponse(
            {
                "status": "OK",
                "message": "User created.",
                "user": {
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            },
            status=201,
        )
