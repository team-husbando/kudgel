from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, BaseListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kudgel.project.models import Project
from kudgel.user.models import User
from kudgel.user.forms import ProjectUserForm
from kudgel.user.serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'generic/form.html'


class CreateProjectUserView(FormView, BaseListView):
    form_class = ProjectUserForm
    model = User
    template_name = 'generic/form.html'
    slug_url_kwarg = 'p_id'
    extra_context = {}
    success_url = reverse_lazy('project')

    def get(self, request, *args, **kwargs):
        self.object_list = Project.objects.filter(
            project__id=self.kwargs.get('p_id'))
        self.extra_context.update({'objects':self.object_list})
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(self.kwargs.get('p_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return '/project/{}/'.format(self.kwargs['p_id'])

class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs.get('slug'))

class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
 
 
class StaffListView(ListView):
    model = User
    slug_url_kwarg = 'p_id'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
 