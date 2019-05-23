from datetime import datetime, timedelta

from django.forms.models import model_to_dict
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from kudgel.shift.helpers import GetCalendar
from kudgel.shift.models import Shift
from kudgel.project.models import Project, Role
from kudgel.project.serializers import ProjectSerializer, RoleSerializer
from kudgel.project.forms import RoleForm, ProjectForm


class SplashView(LoginRequiredMixin, ListView):
    template_name = 'choose_project.html'
    model = Project
    extra_context = {'welcome': 'welcome'}

    def get(self, request, *args, **kwargs):
        self.object_list = self.model.objects.filter(
            owner=request.user) | self.model.objects.filter(
                staff__id=request.user.id)
        context = self.get_context_data()
        return self.render_to_response(context)
    

class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RoleViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleFormView(LoginRequiredMixin, CreateView):
    model = Role
    template_name = 'generic/form.html'
    form_class = RoleForm
    success_url = reverse_lazy('home')


class ProjectFormView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'generic/form.html'
    form_class = ProjectForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.success_url = '/project/{}/'.format(self.object.id)
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = '_id'

    def get(self, request, _id, *args, **kwargs):
        self.object = self.get_object()
        request.session['project_id'] = self.object.id

        context = self.get_context_data(object=self.object, **kwargs)
        context.update(
            {'object_list': Shift.objects.filter(project__id=_id)})

        # get shift in range of calendar
        queryset = Shift.objects.filter(
            project__id=self.object.id,
            date__gte=datetime.today()-timedelta(days=21),
            date__lte=datetime.today()+timedelta(days=21),
        )
        # update the context with shifts
        context.update({'shift_list': queryset})

        # create calendar
        calendar = GetCalendar(queryset)
        today = datetime.today()
        html_cal = calendar.formatmonth(today.year, today.month)
        context.update({'calendar': mark_safe(html_cal)})
        return self.render_to_response(context)
