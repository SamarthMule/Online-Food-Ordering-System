# authentication/models.py

from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('delivery', 'Delivery Personnel'),
        ('restaurant', 'Restaurant Owner'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    # Additional fields for specific roles
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    vehicle_plate_number = models.CharField(max_length=20, blank=True, null=True)
    restaurant_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
