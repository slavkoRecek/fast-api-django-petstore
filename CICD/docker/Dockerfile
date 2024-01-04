
#
FROM python:3.10-bullseye

#
WORKDIR /code

#
COPY requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./CICD/stages /code/CICD/stages
COPY ./static /code/static
COPY ./application /code/application
COPY manage.py /code/manage.py
COPY entrypoint.sh /code/entrypoint.sh

#
# CMD ["uvicorn", "application.asgi:app", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["/code/entrypoint.sh"]

