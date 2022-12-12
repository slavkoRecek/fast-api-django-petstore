# how to run
This project uses pipenv to manage dependencies. To install pipenv, run `pip install pipenv`. 
To install dependencies, run `pipenv install`. 

Here is a cheatsheet for pipenv: https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55

To run have the project properly setup in pycharm. One needs to provide the path to the python interpreter.
You can find the path to the python interpreter by running `pipenv --venv` in the project directory.

Django cheatsheet: https://dev.to/ericchapman/my-beloved-django-cheat-sheet-2056

create new django apps with `python manage.py startapp <app_name>`

To run a postgres database locally, run `docker-compose up -d` in the project directory.
To run the server, run `uvicorn config.asgi:app --reload`

To run the tests, run `python manage.py test --keepdb`
(known issue: test database is not destroyed because fast api has an open connection)

To run it with docker/compose, run `docker-compose up -d --build` in the project directory.

Important urls:
- http://localhost:8000/fast-api/docs
- http://localhost:8000/django/admin
- http://localhost:8000/fast-api/pets


