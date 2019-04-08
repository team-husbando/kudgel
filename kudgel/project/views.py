from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from kudgel.project.models import Project, Role
from kudgel.project.serializers import ProjectSerializer, RoleSerializer
from kudgel.project.forms import RoleForm, ProjectForm


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
