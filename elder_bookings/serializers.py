from rest_framework import serializers
from elder_services.models import bookings

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookings
        fields = '__all__'  # or explicitly list ['id', 'user_id', 'service_id', ...]
