from django import forms
from django.utils import timezone
from elder_services.models import bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model=bookings
        exclude = ['user_id', 'service_id', 'subservice_id', 'price']
        
        labels = {
            'booking_time': 'Preferred Booking Time',
            'from_date': 'Start Date',
            'to_date': 'End Date',
        }

        widgets = {
            'booking_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'value': timezone.now().strftime('%Y-%m-%dT%H:%M'),
            }),
            'from_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'to_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
