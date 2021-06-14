from rest_framework import status
from rest_framework.test import APITestCase
from core_model.models import Patient, Physician, Appointment
from api.views import AppointmentsViewSet
from datetime import datetime, timedelta
from api.tasks import generate_billing
import json


class TasksTest(APITestCase):

    def setUp(self):
        patient = Patient.objects.create(first_name='Orane', last_name='Brousse')
        physician = Physician.objects.create(first_name='Loyal', last_name='Dubé')
        appointment = Appointment.objects.create(patient=patient, physician=physician)
        appointment.end_date = appointment.start_date + timedelta(minutes=90)
        view = AppointmentsViewSet()
        self.id = appointment.id
        self.value = view.calc_value_appointment(appointment)

    def test_generate_billing_exception(self):
        with self.assertRaises(Exception):
            generate_billing(appointment=str(self.id), value=str(self.value))


