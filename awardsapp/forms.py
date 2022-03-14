from .models import Project,Profile
from django.forms import ModelForm
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image','title','description','url')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact')