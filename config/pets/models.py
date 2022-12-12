from django.db import models

# Select Field (return value, display value)
STATUS_CHOICES = (
    ('available', 'available'),
    ('pending', 'pending'),
    ('sold', 'sold'),
)


class Pet(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
