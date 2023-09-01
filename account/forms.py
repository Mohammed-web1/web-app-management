# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# #from django.contrib.auth.models import User
# from .models import User

# class SignUpForm(forms.ModelForm):
#     # email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())

#     class Meta:
#         model=User
#         fields = '__all__'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import rols




class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
    name = forms.CharField( max_length = 20)
    last_name = forms.CharField( max_length = 20)
    role = forms.ChoiceField(choices=rols)
    
    class Meta:
        model=User
        fields = {'name','last_name','role','username','email','password1','password2'}


