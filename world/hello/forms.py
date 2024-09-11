from django import forms # type: ignore
from .models import KYC

class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC # form or model is associated with the KYC model.
        fields = ['first_name', 'last_name', 'dob', 'gender', 'country', 'state', 'town', 'zip_code', 'phone1', 'phone2', 'email']
