from django import forms
from elder_services.models import user_info

class SignupForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields['uname'].label="Username"
        self.fields['pwd'].label="Password"

    class Meta:
        model = user_info
        fields = ("uname","pwd") 

class LoginForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields['uname'].label="Username"
        self.fields['pwd'].label="Password"
    class Meta:
        model = user_info
        fields = ("uname","pwd")