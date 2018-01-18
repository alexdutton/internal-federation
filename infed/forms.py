from django import forms

from . import models
from .validators import validate_metadata


class ServiceProviderForm(forms.ModelForm):
    xml = forms.CharField(label='SAML Metadata XML',
                          widget=forms.Textarea,
                          validators=[validate_metadata])

    class Meta:
        model = models.ServiceProvider
        fields = ('xml',)