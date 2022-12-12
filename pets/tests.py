from django.test import TransactionTestCase
from fastapi.testclient import TestClient

from config.asgi import app
from pets.models import Pet


# Create your tests here.

class FastApiTestCase(TransactionTestCase):
    fast_api_client = TestClient(app)


class ListPetsTestCase(FastApiTestCase):

    def setUp(self) -> None:
        dog = Pet(name='dogy', status='available')
        dog.save()

    def test_list_pets(self):
        response = self.fast_api_client.get("/fast-api/pets")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': 1, 'name': 'dogy', 'status': 'available'}])
        print(response.json())
