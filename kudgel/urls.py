"""kudgel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from kudgel.project.models import Role, Project
from kudgel.shift.models import Shift

from kudgel.project.urls import urlpatterns as project_urls
from kudgel.shift.urls import urlpatterns as shift_urls
from kudgel.user.urls import urlpatterns as user_urls

from kudgel.project.views import ProjectViewSet
from kudgel.shift.views import ShiftViewSet
from kudgel.user.views import UserViewSet

admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Shift)

router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'shift', ShiftViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]

urlpatterns += project_urls
urlpatterns += shift_urls
urlpatterns += user_urls