from django import forms

from landingpage.core.models import Contato


class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = '__all__'
