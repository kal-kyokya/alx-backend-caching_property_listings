from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property


@receiver(post_save, sender=Property)
def invalidate_properties_cache_on_save(sender, instance, **kwargs):
    """Invalidates the 'all_properties' cache key when a Property object is saved (created or updated).
    """
    cache_key = 'all_properties'
    if cache.get(cache_key) is not None:
        cache.delete(cache_key)
        print(f"Cache '{cache_key}' invalidated due to Property save (ID: {instance.id}).")
    else:
        print(f"Cache '{cache_key}' was not found, no invalidation needed.")

@receiver(post_delete, sender=Property)
def invalidate_properties_cache_on_delete(sender, instance, **kwargs):
    """Invalidates the 'all_properties' cache key when a Property object is deleted.
    """
    cache_key = 'all_properties'
    if cache.get(cache_key) is not None:
        cache.delete(cache_key)
        print(f"Cache '{cache_key}' invalidated due to Propert delete (ID: {instance.id}).")
    else:
        print(f"Cache '{cache_key}' was not found, no invalidation needed.")
