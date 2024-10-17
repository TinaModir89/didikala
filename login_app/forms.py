from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import profile
from django.contrib.auth import get_user_model


user = get_user_model()


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = user
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']



class Additional_info(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_picture', 'phone_number', 'national_id', 'card_no' , 'is_Subscription']

    
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = user
        fields = ['first_name' , 'last_name' , 'email']