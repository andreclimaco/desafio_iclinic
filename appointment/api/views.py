from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime, timezone
from core_model.models import Appointment
from .serializers import AppointmentSerializer
from .tasks import generate_billing
from decimal import *


class AppointmentsViewSet(viewsets.ModelViewSet):
    """
    API Appointments: Method GET, POST, PUT, PATCH, DELETE
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    # permission_classes = (permissions.DjangoModelPermissions,)

    @action(methods=['put', 'get'], detail=True)
    def finish(self, request, *args, **kwargs):
        appointment = self.get_object()
        if not appointment.end_date:
            appointment.end_date = datetime.now(tz=timezone.utc)
            appointment.save()
            serializer = AppointmentSerializer(appointment)
            value_appointment = self.calc_value_appointment(appointment)
            generate_billing.delay(appointment=str(
                appointment.id), value=str(value_appointment))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Appointment already finished.', status=status.HTTP_400_BAD_REQUEST)

    def calc_value_appointment(self, appointment):
        """
        Calculate the value of the medical appointment
        """
        total_seconds = (appointment.end_date -
                         appointment.start_date).total_seconds()
        hours = total_seconds // 3600
        minutes = (total_seconds // 60) % 60
        value = appointment.price
        getcontext().prec = 3
        price_minute_mod = Decimal(value) / Decimal(60)
        if hours:
            value = (value * int(hours)) + (price_minute_mod * int(minutes))
        return value
