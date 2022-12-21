#
FROM python:3.10-bullseye as builder

#
WORKDIR /tmp

#
RUN pip install pipenv

#
COPY ./Pipfile ./Pipfile.lock /tmp/

#
RUN pipenv requirements >> requirements.txt

#
FROM python:3.10-bullseye

#
WORKDIR /code

#
COPY --from=builder /tmp/requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./CICD/stages /code/CICD/stages
COPY ./static /code/static
COPY ./application /code/application

#
CMD ["uvicorn", "application.asgi:app", "--host", "0.0.0.0", "--port", "8000"]
