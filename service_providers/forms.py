from django import forms
from samples.models import Service_Provider

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model=Service_Provider
        fields=['service_name','text']
        labels={'text':'','service_name':''}