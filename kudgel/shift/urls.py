from django.urls import path

from kudgel.shift.views import ShiftFormView, ShiftDetailView, ShiftListView, ProjectShiftListView, ProjectShiftDetailView # noqa


urlpatterns = [
    path('project/<slug:p_id>/shift/new/',
         ShiftFormView.as_view(), name='create_shift'),
    path('project/<slug:p_id>/shift/<slug:s_id>/',
         ProjectShiftDetailView.as_view(), name='p_shift_detail'),
    path('project/<slug:p_id>/shift/',
         ProjectShiftListView.as_view(), name='p_shift_list'),
]
