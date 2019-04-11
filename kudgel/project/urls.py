from django.urls import path

from kudgel.project.views import RoleFormView, ProjectFormView, ProjectDetailView, SplashView # noqa


urlpatterns = [
    path('', SplashView.as_view(), name='home'),
    # path('role/', RoleFormView.as_view(), name='create_role'),
    path('project/', ProjectFormView.as_view(), name='create_project'),
    path('project/<int:_id>/', ProjectDetailView.as_view(), name='a_project'),
]
