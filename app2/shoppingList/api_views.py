from .models import ShoppingListItem, ShoppingList
from .serializers import ShoppingList_Serializer, ShoppingListItem_Serializer
from rest_framework import viewsets


class ShoppingList_view_set(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingList_Serializer
    
class ShoppingListItem_view_set(viewsets.ModelViewSet):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItem_Serializer