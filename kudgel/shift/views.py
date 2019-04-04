from django.shortcuts import render
from rest_framework import viewsets
from kudgel.shift.models import Shift
from kudgel.shift.serializers import ShiftSerializer

# Create your views here.


class ShiftViewSet(viewsets.ModelViewSet):

    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
