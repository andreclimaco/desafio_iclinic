from django.contrib import admin
from .models import Patient, Physician, Appointment, Charge

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name'
    )


@admin.register(Physician)
class PhysicianAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name'
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'get_patient_fullname',
        'get_physician_fullname',
        'start_date',
        'end_date'
    )

    def get_patient_fullname(self, obj):
        return f'{obj.patient.first_name} {obj.patient.last_name}'
    get_patient_fullname.short_description = 'Patient'
    get_patient_fullname.admin_order_field = 'patient__fullname'

    def get_physician_fullname(self, obj):
        return f'{obj.physician.first_name} {obj.physician.last_name}'
    get_physician_fullname.short_description = 'Physician'
    get_physician_fullname.admin_order_field = 'physician__fullname'


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = (
        'get_patient_fullname',
        'get_physician_fullname',
        'value',
    )

    def get_patient_fullname(self, obj):
        return f'{obj.appointment.patient.first_name} {obj.appointment.patient.last_name}'
    get_patient_fullname.short_description = 'Patient'
    get_patient_fullname.admin_order_field = 'patient__fullname'

    def get_physician_fullname(self, obj):
        return f'{obj.appointment.physician.first_name} {obj.appointment.physician.last_name}'
    get_physician_fullname.short_description = 'Physician'
    get_physician_fullname.admin_order_field = 'physician__fullname'