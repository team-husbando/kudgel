from django.urls import path

from kudgel.project.views import RoleFormView, ProjectFormView


urlpatterns = [
    path('role/', RoleFormView.as_view(), name='create_role'),
    path('project/', ProjectFormView.as_view(), name='create_project'),
]
