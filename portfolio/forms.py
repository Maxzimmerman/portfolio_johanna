from django import forms
from .models import Service


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name*'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-Mail*'}))
    service = forms.ModelChoiceField(
        queryset=Service.objects.exclude(title='Preise'),
        empty_label="Wähle einen Service",
        widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Nachricht*'}))
