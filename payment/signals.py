from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineProduct


@receiver(post_save, sender=OrderLineProduct)
def update_on_save(sender, instance, created, **kwargs):
    """
    This updates the order total line by updating and creating.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineProduct)
def update_on_delete(sender, instance, **kwargs):
    """
    This updates the order total line by deleting.
    """
    instance.order.update_total()
