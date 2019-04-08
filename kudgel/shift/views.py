from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic.detail import DetailView
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
    template_name = 'generic/form.html'
    form_class = ShiftForm
    sucess_url = reverse_lazy('success')

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request)
        if form.is_valid():
            data = form.cleaned_data
            Shift.objects.create(
                name=data['name'],
                start_time=data['start_time'],
                end_time=data['end_time'],)
        else:
            return render(request, self.template_name, {
                'form': self.form_class})
        return reverse_lazy('success')

class ShiftDetailView(DetailView):

    model = Shift

    def get_object(self, queryset=None):
        return Shift.objects.get(id=self.kwargs.get('slug'))

