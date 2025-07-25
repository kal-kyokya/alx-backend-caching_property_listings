from django.core.cache import cache
from .models import Property


def get_all_properties():
    """Fetches all properties, caching the queryset in Redis for 1 hour.
    """
    cache_key = 'all_properties'
    queryset = cache.get(cache_key)

    if queryset is None:
        print("Fetching all properties from DB...")
        queryset = Property.objects.all()

        cache.set(cache_key, queryset, 3600)
    else:
        print("Serving all properties from cache.")

    return queryset
