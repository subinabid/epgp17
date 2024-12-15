"""Root views for the API Server."""

from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        return JsonResponse(
            {   
                "status": 'OK',
                "message":"Server is running. Call /api/ for API.",
            }, 
            status=200
        )
    
    return JsonResponse(
        {
            "status": 'ERROR',
            "message": "Invalid request method.",
        },
        status=400
    )
