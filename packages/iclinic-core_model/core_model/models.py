import uuid
from django.db import models


class AbstractPerson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)

    class Meta:
        abstract = True


class Patient(AbstractPerson):

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Physician(AbstractPerson):

    class Meta:
        verbose_name = 'Physician'
        verbose_name_plural = 'Physicians'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT)
    physician = models.ForeignKey('Physician', on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(default=200, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        start_date = self.start_date.strftime("%d/%m/%Y %H:%M")
        end_date = ''
        if self.end_date:
            end_date = self.end_date.strftime("%d/%m/%Y %H:%M")
        return f'{start_date}: {end_date}'


class Charge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointment = models.ForeignKey('Appointment', on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Charge'
        verbose_name_plural = 'Charges'

    def __str__(self):
        return f'{self.appointment}: {self.value}'
