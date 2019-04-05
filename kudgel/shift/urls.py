from django.urls import path
from .views import ShiftFormView


urlpatterns = [
    path('shift/', ShiftFormView.as_view(), name='create_shift')
]