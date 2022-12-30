from django.test import TransactionTestCase
from fastapi.testclient import TestClient

from application.asgi import app
from application.pets.models import Pet


# Create your tests here.

class FastApiTestCase(TransactionTestCase):
    fast_api_client = TestClient(app)

    def tearDown(self):
        pass
# self.fast_api_client.close()


class ListPetsTestCase(FastApiTestCase):

    def setUp(self) -> None:
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
        print(response.json())


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
        print(response.json())

    def test_create_pets_with_invalid_status(self):
        response = self.fast_api_client.post(url="/fast-api/pets", json={
            'name': 'dogy',
            'status': 'Invalid'})
        self.assertEqual(response.status_code, 422)
        response: dict = response.json()
        self.assertEqual(response['detail'][0]['msg'],
                         "value is not a valid enumeration member; permitted: \'available\', \'pending\', \'sold\'")
