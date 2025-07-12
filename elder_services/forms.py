from django import forms
from .models import services

class ServiceForm(forms.ModelForm):

    class Meta:
        model=services
        fields=('service_name','service_id')
    
    