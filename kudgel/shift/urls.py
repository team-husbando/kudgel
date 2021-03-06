
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from kudgel.shift.views import ShiftFormView, ProjectShiftDetailView, ProjectShiftListView

urlpatterns = [
    path('project/<slug:p_id>/shift/',
         ShiftFormView.as_view(), name='create_shift'),
    path('project/<slug:p_id>/shift/<slug:s_id>/',
         ProjectShiftDetailView.as_view(), name='p_shift_detail'),
    path('project/<slug:p_id>/shift/cal',
         ProjectShiftListView.as_view(), name='p_shift_list'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
