from rest_framework import viewsets
from .models import Ingredient
from .serializers import ItemSerializer

class Ingredients_view_set(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = ItemSerializer
