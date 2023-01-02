import logging

from httpx import Response

from application.pets.models import Pet
from extra_libs.testing import FastApiTestCase

# Create your tests here.
logger = logging.getLogger(__name__)


class ListPetsTestCase(FastApiTestCase):

    def setUp(self) -> None:
        super().setUp()
        dog = Pet(name='dogy', status='available')
        dog.save()

    def test_list_pets(self):
        response = self.fast_api_client.get("/fast-api/pets")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        pet: dict = response.json()[0]
        self.assertTrue('id' in pet)
        self.assertEqual(pet['name'], 'dogy')
        self.assertEqual(pet['status'], 'available')


class CreatePetsTestCase(FastApiTestCase):

    def test_create_pets(self):
        response = self.fast_api_client.post(url="/fast-api/pets", json={
            'name': 'dogy',
            'status': 'available'})
        self.assertEqual(response.status_code, 201)
        pet: dict = response.json()
        self.assertTrue('id' in pet)
        self.assertEqual(pet['name'], 'dogy')
        self.assertEqual(pet['status'], 'available')

    def test_create_pets_with_invalid_status(self):
        response: Response = self.fast_api_client.post(
            url="/fast-api/pets",
            json={
                'name': 'dogy',
                'status': 'Invalid'
            })
        self.assertEqual(response.status_code, 422)
        response: dict = response.json()
        self.assertEqual(response['status_code'], 422)
        self.assertEqual(len(response['errors']), 1)
        self.assertEqual(response['errors'][0]['message'], "Field 'status' is invalid. value is not a valid enumeration member; permitted: 'available', 'pending', 'sold'")
        self.assertEqual(response['errors'][0]['code'], 'validation_error')
        self.assertEqual(response['errors'][0]['detail'], {
            'model_class': 'PetIn',
            'field': 'status',
        })
