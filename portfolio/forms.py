from django import forms
from .models import Service, PdfTableAdjustedBodyPart
from hcaptcha.fields import hCaptchaField
from django.forms import formset_factory


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name*'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-Mail*'}))
    service = forms.ModelChoiceField(
        queryset=Service.objects.exclude(title='Preise'),
        empty_label="Wähle einen Service",
        widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Nachricht*'}))
    captcha = hCaptchaField(theme="dark", size="compact")


class PdfAdjustedBodyPartsTableForm(forms.Form):
    key = forms.ModelChoiceField(
        PdfTableAdjustedBodyPart.objects.all(),
        empty_label="Wähle ein behandeltes Körperteil aus",
        label="",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    value = forms.CharField(label='', max_length=255 ,widget=forms.TextInput(attrs={'placeholder': 'Behandlungsbeschreibung'}))


class PdfAdjustedBodyPartsLegendTableForm(forms.Form):
    key = forms.ModelChoiceField(
        PdfTableAdjustedBodyPart.objects.all(),
        empty_label="Wähle ein behandeltes Körperteil aus",
        label="",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    value = forms.CharField(label='', max_length=255 ,widget=forms.TextInput(attrs={'placeholder': 'Behandlungsbeschreibung'}))

PdfAdjustedBodyPartsTableFormSet = formset_factory(PdfAdjustedBodyPartsTableForm, extra=0, can_delete=True)
PdfAdjustedBodyPartsLegendTableFormSet = formset_factory(PdfAdjustedBodyPartsLegendTableForm, extra=0, can_delete=True)

class CreatePDfForm(forms.Form):
    costumer_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Kundenname*'}))
    date = forms.DateField(
        label="",
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={'placeholder': 'Datum*'})
    )
    further_movements = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Weitere Bewegungen*'})
    )
    suggestions = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Empfehlun*'})
    )
