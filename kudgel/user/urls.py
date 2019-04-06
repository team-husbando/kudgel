from django.urls import path

from kudgel.user.views import CreateUserView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/join/', CreateUserView.as_view(), name='new_user'),
]
