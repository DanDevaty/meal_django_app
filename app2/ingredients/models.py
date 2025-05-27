from django.db import models
from django.utils.translation import gettext_lazy as _

class Ingredient(models.Model):
    MEASUREMENT_CHOICES = [
        ('g/100', _('per 100 grams')),
        ('ml/100', _('per 100 milliliters')),
    ]

    name = models.CharField(_('Name'), max_length=50, unique=True)
    calories = models.FloatField(_('Calories'))
    fat = models.FloatField(_('Fat'))
    glucose = models.FloatField(_('Glucose'))
    measurement = models.CharField(_('Measurement'), max_length=10, choices=MEASUREMENT_CHOICES, default='g/100')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
