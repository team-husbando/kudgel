from django.urls import path

from kudgel.project.views import RoleFormView, ProjectFormView, ProjectDetailView, HomeView, SplashView # noqa


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('landing/', SplashView.as_view(), name='splash'),
    path('role/', RoleFormView.as_view(), name='create_role'),
    path('project/new/', ProjectFormView.as_view(), name='create_project'),
    path('project/<int:_id>/', ProjectDetailView.as_view(), name='a_project'),
]
