from django import forms
from .models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model= Picture
        fields = ['title','description','image',]
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
