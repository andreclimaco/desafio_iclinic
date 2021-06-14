from django.test import TestCase
from django.db import models
from core_model.models import Patient, Physician, Appointment, Charge

from .base import create_patient, create_physician, create_appointment, create_charge


class PatientModelTest(TestCase):

    def test_field_first_name(self):
        field = Patient._meta.get_field('first_name')
        self.assertEquals(isinstance(field, models.CharField), True)
        self.assertEquals(field.verbose_name, 'first name')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.max_length, 100)

    def test_field_last_name(self):
        field = Patient._meta.get_field('last_name')
        self.assertEquals(isinstance(field, models.CharField), True)
        self.assertEquals(field.verbose_name, 'last name')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.max_length, 100)

    def test_create_patient(self):
        first_name = 'Loyal'
        last_name = 'Dubé'
        fullname = f'{first_name} {last_name}'
        patient = create_patient(first_name, last_name)
        self.assertTrue(isinstance(patient, Patient))
        self.assertEqual(patient.__str__(), fullname)


class PhysicianModelTest(TestCase):

    def test_field_first_name(self):
        field = Physician._meta.get_field('first_name')
        self.assertEquals(isinstance(field, models.CharField), True)
        self.assertEquals(field.verbose_name, 'first name')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.max_length, 100)

    def test_field_last_name(self):
        field = Physician._meta.get_field('last_name')
        self.assertEquals(isinstance(field, models.CharField), True)
        self.assertEquals(field.verbose_name, 'last name')
        self.assertEquals(field.null, False)
        self.assertEquals(field.blank, False)
        self.assertEquals(field.max_length, 100)

    def test_create_physician(self):
        first_name = 'Alita'
        last_name = 'Boucher'
        fullname = f'{first_name} {last_name}'
        patient = create_physician(first_name, last_name)
        self.assertTrue(isinstance(patient, Physician))
        self.assertEqual(patient.__str__(), fullname)


class AppointmentModelTest(TestCase):

    def test_field_patient(self):
        field = Appointment._meta.get_field('patient')
        self.assertEquals(isinstance(field, models.ForeignKey), True)
        self.assertEquals(field.related_model, Patient)

    def test_field_physician(self):
        field = Appointment._meta.get_field('physician')
        self.assertEquals(isinstance(field, models.ForeignKey), True)
        self.assertEquals(field.related_model, Physician)

    def test_field_start_date(self):
        field = Appointment._meta.get_field('start_date')
        self.assertEquals(isinstance(field, models.DateTimeField), True)
        self.assertTrue(field.auto_now_add)

    def test_field_end_date(self):
        field = Appointment._meta.get_field('end_date')
        self.assertEquals(isinstance(field, models.DateTimeField), True)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_field_price(self):
        field = Appointment._meta.get_field('price')
        self.assertEquals(isinstance(field, models.DecimalField), True)
        self.assertEquals(field.default, 200)
        self.assertEquals(field.max_digits, 10)
        self.assertEquals(field.decimal_places, 2)

    def test_create_appointment(self):
        appointment = create_appointment()
        start_date = appointment.start_date.strftime("%d/%m/%Y %H:%M: ")
        self.assertTrue(isinstance(appointment, Appointment))
        self.assertEqual(appointment.__str__(), start_date)

    def test_create_appointment_end_date(self):
        appointment = create_appointment(end_date=True)
        start_date = appointment.start_date.strftime("%d/%m/%Y %H:%M")
        end_date = appointment.end_date.strftime("%d/%m/%Y %H:%M")
        date = f'{start_date}: {end_date}'
        self.assertTrue(isinstance(appointment, Appointment))
        self.assertEqual(appointment.__str__(), date)


class ChargeModelTest(TestCase):

    def test_field_appointment(self):
        field = Charge._meta.get_field('appointment')
        self.assertEquals(isinstance(field, models.ForeignKey), True)
        self.assertEquals(field.related_model, Appointment)

    def test_field_value(self):
        field = Charge._meta.get_field('value')
        self.assertEquals(isinstance(field, models.DecimalField), True)
        self.assertEquals(field.max_digits, 10)
        self.assertEquals(field.decimal_places, 2)

    def test_create_charge(self):
        charge = create_charge()
        start_date = charge.appointment.start_date.strftime("%d/%m/%Y %H:%M")
        end_date = charge.appointment.end_date.strftime("%d/%m/%Y %H:%M")
        self.assertTrue(isinstance(charge, Charge))
        self.assertEqual(charge.__str__(), f'{start_date}: {end_date}: {charge.value}')