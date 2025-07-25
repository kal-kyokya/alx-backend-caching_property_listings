from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
import json # For pretty printing JSON if needed for debugging, though JsonResponse handles serialization


# Cache the view for 15 minutes (60 seconds * 15 = 15 minutes)
@cache_page(60 * 15)
def property_list(request):
    """Handles requests for all property records stored in DB.
    Args:
    	request: request object coming from the client-side. More technically stated: 'It encapsulates all the information about the incoming web request.'
    Return:
    	Returns a list of all properties, with the response cached in Redis.
    """
    # Fetch all properties from the database
    properties = Property.objects.all()

    # Convert QuerySet to a list of dictionaries (simple serialization)
    data = []
    for prop in properties:
        data.append({
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'price': prop.price,
            'location': prop.location,
            'created_at': prop.created_at,
        })

    # Return as JSON response
    # 'safe=False' is needed when returning a list (not a dict)
    # Instead of return JsonResponse({})
    return JsonResponse(data, safe=False)
