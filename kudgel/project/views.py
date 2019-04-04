from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from kudgel.project.models import Project
from kudgel.project.serializers import ProjectSerializer

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
