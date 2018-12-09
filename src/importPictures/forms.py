from django import forms
from importPictures.models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model=Facture
        fields= '__all__'
