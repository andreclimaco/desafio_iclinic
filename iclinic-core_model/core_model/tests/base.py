from core_model.models import Patient, Physician, Appointment, Charge
from datetime import datetime
import pytz


def create_patient(first_name, last_name):
    return Patient.objects.create(first_name=first_name, last_name=last_name)


def create_physician(first_name, last_name):
    return Physician.objects.create(first_name=first_name, last_name=last_name)


def create_appointment(end_date=False):
    patient = create_patient(first_name='Avice', last_name='Charpentier')
    physician = create_physician(first_name='Troy', last_name='Cloutier')
    if not end_date:
        return Appointment.objects.create(patient=patient, physician=physician)
    else:
        return Appointment.objects.create(patient=patient, physician=physician, end_date=datetime.now(pytz.UTC))


def create_charge():
    appointment = create_appointment(end_date=True)
    return Charge.objects.create(appointment=appointment, value=200.00)