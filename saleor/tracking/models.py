from django.db import models
from ..order.models import Order
from . import TrackingStatus
from django.conf import settings


class Shipping(models.Model):
    created = models.DateTimeField()
    status = models.CharField(
        max_length=16, default=TrackingStatus.PREPARING, choices=TrackingStatus.CHOICES
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="shippings",
        on_delete=models.SET_NULL,
    )

    order = models.ForeignKey(
        Order,
        related_name="shippings",
        on_delete=models.DO_NOTHING
    )

    tracking_client_id = models.CharField(max_length=32, blank=False)
    tracking_number = models.CharField(max_length=32, blank=False)


class ShippingTracking(models.Model):
    pass
