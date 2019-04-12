from django import forms

from kudgel.project.models import Project, Role


class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = '__all__'


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = '__all__'