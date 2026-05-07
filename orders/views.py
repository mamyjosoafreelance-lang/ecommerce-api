from .serializers import OrderItemSerializer
from .models import OrderItem
from rest_framework.permissions import IsAuthenticated
from cores.permissions import IsOwner
from rest_framework import viewsets


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsOwner, IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user)







