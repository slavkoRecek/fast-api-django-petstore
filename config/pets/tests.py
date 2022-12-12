from django.test import TransactionTestCase
from fastapi.testclient import TestClient

from config.asgi import app
from config.pets.models import Pet


# Create your tests here.

class FastApiTestCase(TransactionTestCase):
    fast_api_client = TestClient(app)

    def tearDown(self):
        self.fast_api_client.close()


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
