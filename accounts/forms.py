from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model
 
User = get_user_model()

class SignupForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    class Meta:
        model = User
        fields = ("username", "full_name", "furigana", "postal_code", "prefecture", "city", "street_address", "building_name", "telephone_number", "gender", "date_of_birth", "privacy_policy_agreement")

class LoginForm(AuthenticationForm):
    pass
    # 継承のみ