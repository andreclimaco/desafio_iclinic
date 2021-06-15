from rest_framework import status
from rest_framework.test import APITestCase
from core_model.models import Patient, Physician, Appointment, Charge
from datetime import datetime, timezone


def create_appointment():
    patient = Patient.objects.create(first_name='Orane', last_name='Brousse')
    physician = Physician.objects.create(first_name='Loyal', last_name='Dubé')
    return Appointment.objects.create(patient=patient, physician=physician, end_date=datetime.now(tz=timezone.utc))


def create_item(client):
    appointment = create_appointment()
    endpoint = '/api/v1/charges/'
    data = dict(appointment=str(appointment.id),
                value='200.00')
    return client.post(endpoint, data, format='json')


def update_item(client, response_create, id):
    endpoint = f'/api/v1/charges/{id}/'
    response_create.json()['value'] = '150.00'
    data = response_create.json()
    return client.put(endpoint, data, format='json')


def patch_item(client, id):
    endpoint = f'/api/v1/charges/{id}/'
    data = dict(value='300.00')
    return client.patch(endpoint, data, format='json')


def delete_item(client, id):
    endpoint = f'/api/v1/charges/{id}/'
    return client.delete(endpoint)


class ChargesAPITest(APITestCase):

    def setUp(self):
        self.response = create_item(self.client)

    def test_item_was_created(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Charge.objects.count(), 1)

    def test_item_was_updated(self):
        response_update = update_item(self.client, self.response, self.response.json().get('id'))
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json().get('value'), '150.00')

    def test_item_was_patch(self):
        response_patch = patch_item(self.client, self.response.json().get('id'))
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(response_patch.json().get('value'), '300.00')

    def test_the_item_was_deleted(self):
        response_delete = delete_item(self.client, self.response.json().get('id'))
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Charge.objects.count(), 0)
