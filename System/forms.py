from django import forms
from System.models import UserProfile, Patient
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = {"name", "telephone", "notes"}
