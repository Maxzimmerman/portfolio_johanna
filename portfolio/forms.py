from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name*'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'E-Mail*'}))
    message = forms.CharField(label="", max_length=300, widget=forms.Textarea(attrs={'placeholder': 'Nachricht'}))
