from django.urls import path

from kudgel.user.views import CreateUserView

urlpatterns = [
    path('join/', CreateUserView.as_view(), name='new_user'),
]
