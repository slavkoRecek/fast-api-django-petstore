from django.db import models


class Status(models.TextChoices):
    AVAILABLE = 'available', 'available'
    PENDING = 'pending', 'pending'
    SOLD = 'sold', 'sold'


class Pet(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.AVAILABLE)

    class Meta:
        db_table = 'pets'
