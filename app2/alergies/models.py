from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Allergy(models.Model):
    ListOfAllergies = [
        (_('Moluscs'), _('Moluscs')),
        (_('Eggs'), _('Eggs')),
        (_('Fish'), _('Fish')),
        (_('Lupin'), _('Lupin')),
        (_('Soya'), _('Soya')),
        (_('Milk'), _('Milk')),
        (_('Peanuts'), _('Peanuts')),
        (_('Gluten'), _('Gluten')),
        (_('Crustaceans'), _('Crustaceans')),
        (_('Mustard'), _('Mustard')),
        (_('Nuts'), _('Nuts')),
        (_('Sesame'), _('Sesame')),
        (_('Celery'), _('Celery')),
        (_('Sulphite'), _('Sulphite')),
        (_('Eggplant'), _('Eggplant')),
        (_('Carrots'), _('Carrots')),
        (_('Peas'), _('Peas')),
        (_('Tomatoes'), _('Tomatoes')),
        (_('Coriander'), _('Coriander')),
        (_('Citrus'), _('Citrus')),
        (_('Berries'), _('Berries')),
        (_('Bananas'), _('Bananas')),
        (_('Garlic'), _('Garlic')),
        (_('Onions'), _('Onions')),

    ]

    name = models.CharField(_('Name'), max_length=100, choices=ListOfAllergies, unique=True)
    addDifAllergies = models.CharField(_('Add different allergy'), max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.name
