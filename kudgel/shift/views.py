from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.safestring import mark_safe

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kudgel.project.forms import RoleForm
from kudgel.user.forms import UserForm
from kudgel.shift.helpers import GetCalendar
from kudgel.shift.models import Shift
from kudgel.shift.forms import ShiftForm
from kudgel.shift.serializers import ShiftSerializer

# Create your views here.


class ShiftViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftFormView(LoginRequiredMixin, CreateView):
    model = Shift
    form_class = ShiftForm
    extra_context = { 'u_form': UserForm, 'r_form': RoleForm }
    sucess_url = reverse_lazy('success')

    # def get(self, request, p_id):
    #     return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, p_id):
        form = self.form_class(request)
        if form.is_valid():
            form.project = p_id
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


class ShiftListView(ListView):

    model = Shift

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProjectShiftDetailView(DetailView):
    model = Shift

    def get_object(self, queryset=None):
        return Shift.objects.get(
            id=self.kwargs.get('s_id'), project__id=self.kwargs.get('p_id'))


class ProjectShiftListView(ListView):
    model = Shift

    def get(self, request, *args, **kwargs):
        self.object_list = self.model.objects.filter(
            project__id=self.kwargs.get('p_id'))
        context = self.get_context_data()

        today = datetime.today()
        cal = GetCalendar(self.object_list)
        html_calendar = cal.formatmonth(today.year, today.month, withyear=True)
        context.update({'cal': mark_safe(html_calendar)})

        return self.render_to_response(context)
