from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from .form import BookingForm
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def menu(request):
    menu_item = models.MenuItems.objects.all()
    menu_serializer = serializers.MenuSerializer
    return render(request, 'menu.html', {'menu' : menu_item})


@csrf_exempt
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            lf = models.Booking(
                name = cd['name'],
                no_of_guests = cd['no_of_guests'],
                booking_date = cd['booking_date'],
            )
            
            lf.save()
    return render(request, 'book.html', {'form': form})


# class MenuItemView(generics.ListCreateAPIView):
#     queryset = models.MenuItems.objects.all()
#     serializer_class  = serializers.MenuSerializer
#     renderer_classes = [JSONRenderer]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.MenuItems.objects.all()
    serializer_class = serializers.MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    



class UserViewSet(viewsets.ModelViewSet):
    queryset = User
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]