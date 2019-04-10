from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
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
    success_url = reverse_lazy('splash')
    template_name = 'generic/form.html'


class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs.get('slug'))

class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
 