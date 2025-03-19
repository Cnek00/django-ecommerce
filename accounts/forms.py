from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Şifreyi Onayla", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_password2(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        return self.cleaned_data["password2"]

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'phone', 'address', 'birth_date']

