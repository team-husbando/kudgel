from django.urls import path
from .views import ShiftFormView, ShiftDetailView, ShiftListView


urlpatterns = [
    path('shift/new/', ShiftFormView.as_view(), name='create_shift'),
    path('shift/<slug:slug>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('shift/', ShiftListView.as_view(), name='shift-list')
]
