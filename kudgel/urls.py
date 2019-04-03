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
from django.urls import path
from kudgel.user.models import Role, User
from kudgel.shift.models import Shift
from kudgel.project.models import Project

from kudgel.project.urls import urlpatterns as projecturls
from kudgel.shift.urls import urlpatterns as shifturls
from kudgel.user.urls import urlpatterns as userurls

admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Shift)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += projecturls
urlpatterns += shifturls
urlpatterns += userurls