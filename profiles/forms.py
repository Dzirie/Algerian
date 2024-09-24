from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['username']
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
