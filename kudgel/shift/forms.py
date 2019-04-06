from django import forms

from kudgel.shift.widgets import BootstrapDateTimePickerInput


class ShiftForm(forms.Form):

    name = forms.CharField(max_length=50)

    start_time = forms.DateTimeField(
        widget=BootstrapDateTimePickerInput, input_formats=['%d/%m/%Y %H:%M'])

    end_time = forms.DateTimeField(
        widget=BootstrapDateTimePickerInput, input_formats=['%d/%m/%Y %H:%M'])
