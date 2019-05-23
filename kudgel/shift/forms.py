from django.forms import ModelForm
from django.forms import TextInput, TimeInput, DateInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from kudgel.shift.models import Shift


class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        exclude = ('project', 'all_day')
        widgets = {
            'start': TimeInput(attrs={'type': 'time',
                                      'class': 'timepicker'}),
            'end': TimeInput(attrs={'type': 'time',
                                    'class': 'timepicker'}),
            'date': DateInput(attrs={'type': 'date',
                                     'class': 'datepicker'}),
        }
