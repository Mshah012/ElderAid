# elder_bookings/api_views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elder_services.models import bookings
from .serializers import BookingSerializer

@api_view(['GET', 'POST'])
def booking_list_create(request,id):
    if request.method == 'GET':
        bookings_qs = bookings.objects.all()
        serializer = BookingSerializer(bookings_qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
