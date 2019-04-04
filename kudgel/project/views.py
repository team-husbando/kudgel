from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kudgel.project.models import Project, Role
from kudgel.project.serializers import ProjectSerializer
from kudgel.project.forms import RoleForm


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RoleFormView(LoginRequiredMixin, CreateView):
    model = Role
    template_url = 'role_form.html'
    form_class = RoleForm
    sucess_url = reverse_lazy('success')
