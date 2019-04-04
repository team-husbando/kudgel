from django.urls import path
from .views import RoleFormView


urlpatterns = [
    path('role/', RoleFormView.as_view(), name='create_role')
]
