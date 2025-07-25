# from django.shortcuts import render
# from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties


# Caching is handled by 'get_all_properties()' at a lower level
def property_list(request):
    """Using a low-level cached utility, handles requests for all property records stored in DB.
    Args:
    	request: request object coming from the client-side. More technically stated: 'It encapsulates all the information about the incoming web request.'
    Return:
    	Returns a list of all properties.
    """
    # Use the utility function to get properties, which handles caching internally
    properties = get_all_properties()

    # Convert QuerSet to a list of dictionaries for JSON response
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

"""
# Cache the view for 15 minutes (60 seconds * 15 = 15 minutes)
@cache_page(60 * 15)
def property_list(request):
    '''Handles requests for all property records stored in DB.
    Args:
    	request: request object coming from the client-side. More technically stated: 'It encapsulates all the information about the incoming web request.'
    Return:
    	Returns a list of all properties, with the response cached in Redis.
    '''
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
"""
