from django.forms import ModelForm
from django.forms import TextInput
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from kudgel.shift.models import Shift


class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        exclude = ('project','all_day')
        widgets = {
            'start': TextInput(attrs={'id': 'start',
                'class':'form-control input-small'}),
            'end': TextInput(attrs={'id': 'end',
                'class':'form-control input-small'}),
        }