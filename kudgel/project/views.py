from django.shortcuts import render
from rest_framework import viewsets
from kudgel.project.models import Project
from kudgel.project.serializers import ProjectSerializer

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
