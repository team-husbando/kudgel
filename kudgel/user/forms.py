from django.forms import ModelForm, Form
from django import forms

from kudgel.user.models import User
from kudgel.project.models import Project

# to create temp password
from secrets import choice
from string import ascii_letters, digits

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    

class ProjectUserForm(Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, p_id):
        alphabet = ascii_letters + digits
        data = self.cleaned_data
        project = Project.objects.get(id=int(p_id))
        user = User.objects.create_user(
            username= data['username'],
            first_name= data['first_name'],
            last_name=data['last_name'],
            email=data['email'],)

        user.email_user('Join our team!','You have been invited to join a team at {{orgname}} by {{adminname}}')
        project.staff.add(user)

        return user