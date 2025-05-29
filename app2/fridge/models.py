from django.db import models
from django.conf import settings
from datetime import date
from django.utils import timezone


class FridgeItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fridge_items', default=None)
    name = models.CharField(max_length=100, default=None)
    quantity = models.PositiveIntegerField(default=1)
    expiration_date = models.DateField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.expiration_date and self.expiration_date < date.today()

    def __str__(self):
        return f"{self.name} x{self.quantity}"


class WatchedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watched_items')
    name = models.CharField(max_length=100)
    min_quantity = models.PositiveIntegerField(default=1)  # pod tuto hranici se přidá do shopping listu

    def __str__(self):
        return f"Watch {self.name} (min: {self.min_quantity})"
