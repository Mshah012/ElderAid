from django import forms
from elder_services.models import sub_services

class SubserviceForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(SubserviceForm,self).__init__(*args,**kwargs)
        self.fields['service_id'].empty_label="Select Service"
        self.fields['service_id'].label="Services"
    
    class Meta:
        model=sub_services
        fields=('subservice_name','subservice_id','price','image','service_id')