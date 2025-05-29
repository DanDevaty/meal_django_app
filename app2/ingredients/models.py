from django.db import models
from django.utils.translation import gettext_lazy as _

class Ingredient(models.Model):
    MEASUREMENT_CHOICES = [
        ('g/100', _('per 100 grams')),
        ('ml/100', _('per 100 milliliters')),
    ]

    name = models.CharField(_('Name'), max_length=50, unique=True)
    calories = models.FloatField(_('Calories'))
    protein = models.FloatField(_('Protein'), default=0.0)
    fat = models.IntegerField(_("Fat"), default=0.0)
    saturated_fat = models.FloatField(_('Saturated Fat'), default=0.0)
    sugar = models.FloatField(_('Sugar'), default=0.0)
    fiber = models.FloatField(_('Fiber'), default=0.0)
    salt = models.FloatField(_('Salt'), default=0.0)
    carbohydrates = models.FloatField(_('Carbohydrates'), default=0.0)
    measurement = models.CharField(_('Measurement'), max_length=10, choices=MEASUREMENT_CHOICES, default='g/100')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
