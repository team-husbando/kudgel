from django.urls import path
from .views import ShiftFormView, ShiftDetailView, ShiftListView
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('shift/new/', ShiftFormView.as_view(), name='create_shift'),
    path('shift/<slug:slug>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('shift/', ShiftListView.as_view(), name='shift-list'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
