from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kudgel.user.models import User
from kudgel.user.serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'generic.form.html'
