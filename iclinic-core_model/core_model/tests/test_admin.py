from django.test import TestCase
from core_model.models import Patient, Physician, Appointment, Charge
from core_model.admin import AppointmentAdmin, ChargeAdmin
from django.contrib.admin.sites import AdminSite, site as default_site

from .base import create_appointment, create_charge


class AppointmentAdminTest(TestCase):

    def test_patient_fullname(self):
        admin = AppointmentAdmin(Appointment, default_site)
        obj = create_appointment()
        fullname = f'{obj.patient.first_name} {obj.patient.last_name}'
        self.assertEquals(admin.get_patient_fullname(obj), fullname)

    def test_physician_fullname(self):
        admin = AppointmentAdmin(Appointment, default_site)
        obj = create_appointment()
        fullname = f'{obj.physician.first_name} {obj.physician.last_name}'
        self.assertEquals(admin.get_physician_fullname(obj), fullname)


class ChargeAdminTest(TestCase):

    def test_patient_fullname(self):
        admin = ChargeAdmin(Charge, default_site)
        obj = create_charge()
        fullname = f'{obj.appointment.patient.first_name} {obj.appointment.patient.last_name}'
        self.assertEquals(admin.get_patient_fullname(obj), fullname)

    def test_physician_fullname(self):
        admin = ChargeAdmin(Charge, default_site)
        obj = create_charge()
        fullname = f'{obj.appointment.physician.first_name} {obj.appointment.physician.last_name}'
        self.assertEquals(admin.get_physician_fullname(obj), fullname)
