"""API Endpoints"""

from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        return JsonResponse(
            {
                "status": 'OK',
                "message": "API is running.",
                "version": "1.0.0"
            }, 
            status=200
            )
    
    return JsonResponse(
        {   
            "status": 'ERROR',
            "message": "Invalid request method."
        }, 
        status=405
        )
