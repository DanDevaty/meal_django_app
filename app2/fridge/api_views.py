from rest_framework import viewsets
from .models import FridgeItem
from .serializers import FridgeItemSerializer

class FridgeItem_view_set(viewsets.ModelViewSet):
    queryset = FridgeItem.objects.all()
    serializer_class = FridgeItemSerializer
