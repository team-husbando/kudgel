from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from kudgel.shift.models import Shift
from kudgel.project.models import Project, Role
from kudgel.project.serializers import ProjectSerializer, RoleSerializer
from kudgel.project.forms import RoleForm, ProjectForm


class SplashView(LoginRequiredMixin, ListView):
    template_name = 'choose_project.html'
    model = Project

    def get(self, request, *args, **kwargs):
        self.object_list = self.model.objects.filter(
            owner=request.user, staff__id=request.user.id)
        context = self.get_context_data()
        return self.render_to_response(context)


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['project'] = request.session.get('project') or 'Welcome'
        print(context)
        if context.get('project_id'):
            queryset = Shift.objects.filter(
                project__id=context['project_id'],
                date__gte=datetime.today()-timedelta(days=21),
                date__lte=datetime.today()+timedelta(days=21),
            )
            print(queryset)
            context.update({'object_list': queryset})

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
    success_url = reverse_lazy('home')


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = '_id'

    def get(self, request, _id, *args, **kwargs):
        request.session.update(
            {'project_id': _id})
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context.update(
            {'object_list': Shift.objects.filter(project__id=_id)})
        print(context)
        return self.render_to_response(context)
