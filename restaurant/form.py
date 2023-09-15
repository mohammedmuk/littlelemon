from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']