# This project demonstrates the 'marriage' of Django and FastAPI

We do use FastAPI mostly with sync views. The motivation for this is to use FastAPI only for the REST layer and Django for the rest of the application. 
## Setup
Create a virtual environment and activate it. 
```shell
virtualenv venv
source venv/bin/activate
```
Install the dependencies
```shell
pip install -r requirements.txt
```


To run the server, run 
```shell
uvicorn application.asgi:app --host 0.0.0.0 --port 8000 --reload
```

### Pycharm
To run have the project properly setup in pycharm. One needs to provide the path to the python interpreter.

### Docker
To run it with docker/compose, run 
```shell
docker compose up -d --build
``` 
in the project directory.
The compose includes a local postgres database. To connect to the database.

### Running tests:
```shell
python manage.py test --keepdb
```
We use a custom test case to run the tests. `FastApiTestCase`

## Important urls:
- http://localhost:8000/fast-api/docs
- http://localhost:8000/django/admin
- http://localhost:8000/fast-api/pets

## Cheat sheets
Django cheatsheet: https://dev.to/ericchapman/my-beloved-django-cheat-sheet-2056

FastApi cheatsheet: https://lyz-code.github.io/blue-book/fastapi/


