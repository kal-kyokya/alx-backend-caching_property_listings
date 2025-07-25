from django.core.cache import cache
from .models import Property
import logging


# Get a logger instance
logger = logging.getLogger(__name__)

def get_all_properties():
    """Fetches all properties, caching the queryset in Redis for 1 hour.
    """
    cache_key = 'all_properties'
    queryset = cache.get(cache_key)

    if queryset is None:
        print("Fetching all properties from DB...") # For demonstration, will show in console
        queryset = Property.objects.all()

        cache.set(cache_key, queryset, 3600)
    else:
        print("Serving all properties from cache.") # For demonstration

    return queryset


def get_redis_cache_metrics():
    """Connects to Redis and retrieves/logs keyspace hit/miss metrics.
    Args:
    	None
    Return:
    	Hits, misses, hit ratio.
    """
    try:
        # Get the underlying Redis client from django_redis
        # '0' indicates the default Redis DB used by django_redis if configured
        # with `LOCATION` for a specific database number like `.../1`
        redis_client = cache.get_client('default')

        # Get Redis INFO, which contains various statistics
        info = redis_client.info()

        # Extract hit and miss counts
        keyspace_hits = info.get('keyspace_hits', 0)
        keyspace_misses = info.get('keyspace_misses', 0)

        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = (keyspace_hits / total_requests) * 100 if total_requests > 0 else 0

        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'total_requests': total_requests,
            'hit_ratio': round(hit_ratio, 2) # Round to 2 decimal places
        }

        logger.info(f"Redis Cache Metrics: Hits={keyspace_hits}, Misses={keyspace_misses}", f"Total Requests={total_requests}, Hit Ratio={hit_ratio:.2f}%")

        return metrics

    except Exception as err:
        logger.error(f"Error retrieving Redis cache metrics: {err}")

        return {
            'keyspace_hits': 0,
            'keyspace_misses': 0,
            'hit_ratio': 0,
            'error': str(err)
        }
