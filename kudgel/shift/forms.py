from django import forms
from .models import Shift


class ShiftForm(forms.Form):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput, input_formats='%Y-%m-%d %H:%M:%S')
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput, input_formats='%Y-%m-%d %H:%M:%S')
