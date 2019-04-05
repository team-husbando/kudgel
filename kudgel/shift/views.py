from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from kudgel.shift.models import Shift
from kudgel.shift.forms import ShiftForm
from kudgel.shift.serializers import ShiftSerializer

# Create your views here.


class ShiftViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftFormView(LoginRequiredMixin, View):
    model = Shift
    template_name = 'shift/shift_form.html'
    form_class = ShiftForm
    sucess_url = reverse_lazy('success')
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

