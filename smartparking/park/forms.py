# forms.py
from django import forms
from .models import VehicleLog

class VehicleLogForm(forms.ModelForm):
    class Meta:
        model = VehicleLog
        fields = ['vehicle_no', 'name', 'phone_no', 'date_and_time', 'duration']
