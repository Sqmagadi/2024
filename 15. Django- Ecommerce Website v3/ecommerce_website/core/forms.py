from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        

class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
        
class UpdateUserPassword(SetPasswordForm):
    password = None
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']