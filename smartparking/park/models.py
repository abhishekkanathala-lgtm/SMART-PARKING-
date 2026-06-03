# models.py
from django.db import models

class VehicleLog(models.Model):
    vehicle_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    date_and_time = models.DateTimeField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.vehicle_no} - {self.name}"
