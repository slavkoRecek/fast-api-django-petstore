from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Phone', max_length=20, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'User({self.id}): <{self.email}>'

    class Meta:
        db_table = 'users'
