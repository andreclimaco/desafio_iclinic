from rest_framework import viewsets, permissions
from rest_framework import filters
from core_model.models import Charge
from .serializers import ChargeSerializer


class ChargesViewSet(viewsets.ModelViewSet):
    """
    API Charges: Method GET, POST, PUT, DELETE
    """
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    # permission_classes = (permissions.DjangoModelPermissions,)
