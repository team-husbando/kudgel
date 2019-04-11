from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
# from kudgel.shift.widgets import BootstrapDateTimePickerInput


class ShiftForm(forms.Form):

    name = forms.CharField(max_length=50)
    description = forms.CharField()
    all_day = forms.BooleanField()
    date = forms.DateField(widget=AdminDateWidget)
    start_time = forms.DateTimeField(
        widget=AdminTimeWidget)

    end_time = forms.DateTimeField(
        widget=AdminTimeWidget)
        # BootstrapDateTimePickerInput, input_formats=['%d/%m/%Y %H:%M']
