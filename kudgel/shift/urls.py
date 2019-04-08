from django.urls import path
from .views import ShiftFormView, ShiftDetailView


urlpatterns = [
    path('shift/', ShiftFormView.as_view(), name='create_shift'),
    path('shift/<slug:slug>/', ShiftDetailView.as_view(), name='shift-detail')
]
