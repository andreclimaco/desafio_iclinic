from rest_framework import status
from rest_framework.test import APITestCase
from core_model.models import Patient, Physician, Appointment
from api.views import AppointmentsViewSet
from datetime import timedelta


def create_item(client):
    patient = Patient.objects.create(first_name='Orane', last_name='Brousse')
    physician = Physician.objects.create(first_name='Loyal', last_name='Dubé')
    endpoint = '/api/v1/appointments/'
    data = dict(patient=patient.id,
                physician=physician.id)
    return client.post(endpoint, data, format='json')


def update_item(client, response_create, id):
    endpoint = f'/api/v1/appointments/{id}/'
    response_create.json()['price'] = '150.00'
    data = response_create.json()
    return client.put(endpoint, data, format='json')


def patch_item(client, id):
    endpoint = f'/api/v1/appointments/{id}/'
    data = dict(price='300.00')
    return client.patch(endpoint, data, format='json')


def delete_item(client, id):
    endpoint = f'/api/v1/appointments/{id}/'
    return client.delete(endpoint)


def finish_appointment(client, id):
    endpoint = f'/api/v1/appointments/{id}/finish/'
    return client.put(endpoint)


class AppointmentAPITest(APITestCase):

    def setUp(self):
        self.response = create_item(self.client)

    def test_item_was_created(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 1)

    def test_item_was_updated(self):
        response_update = update_item(self.client, self.response, self.response.json().get('id'))
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json().get('price'), '150.00')

    def test_item_was_patch(self):
        response_patch = patch_item(self.client, self.response.json().get('id'))
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(response_patch.json().get('price'), '300.00')

    def test_the_item_was_deleted(self):
        response_delete = delete_item(self.client, self.response.json().get('id'))
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appointment.objects.count(), 0)

    def test_item_was_finished(self):
        id = self.response.json().get('id')
        response_finish = finish_appointment(self.client, id)
        self.assertEqual(response_finish.status_code, status.HTTP_200_OK)
        self.assertIsNot(response_finish.json().get('end_date'), None)

    def test_finished_received_400_status_code(self):
        id = self.response.json().get('id')
        finish_appointment(self.client, id)
        response_finish = finish_appointment(self.client, id)
        self.assertEqual(response_finish.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calc_value_appointment(self):
        patient = Patient.objects.create(first_name='Orane', last_name='Brousse')
        physician = Physician.objects.create(first_name='Loyal', last_name='Dubé')
        appointment = Appointment.objects.create(patient=patient, physician=physician)
        appointment.end_date = appointment.start_date + timedelta(minutes=90)
        view = AppointmentsViewSet()
        value = view.calc_value_appointment(appointment)
        self.assertEqual(value, 300)