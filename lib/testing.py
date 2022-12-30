from django.conf import settings
from django.db import connections
from django.test import TransactionTestCase
from starlette.testclient import TestClient

from application.asgi import app


class FastApiTestCase(TransactionTestCase):
    fast_api_client: TestClient

    def setUp(self) -> None:
        super().setUp()
        self.fast_api_client = TestClient(app)

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass is called')
        cls.close_db_connections()
        super().tearDownClass()

    @classmethod
    def close_db_connections(cls):
        for conn in connections.all():
            with conn.cursor() as cursor:
                cursor.execute(
                    f"""SELECT
                    pg_terminate_backend(pid) FROM pg_stat_activity WHERE
                    pid <> pg_backend_pid() AND
                    pg_stat_activity.datname =
                      '{settings.DATABASES["default"]["NAME"]}';"""
                )
                print(f"Killed {len(cursor.fetchall())} stale connections.")
