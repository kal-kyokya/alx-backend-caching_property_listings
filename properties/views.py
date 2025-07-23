from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
import jsob

@cache_page(60 * 15)
def property_list(request):
    """Returns a list of all properties, with the response cached in Redis."""
    properties = Property.objects.all()

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

    return JsonResponse(data, safe=False)
