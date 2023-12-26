from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model
 
User = get_user_model()

class InputForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    GENDER_CHOICES = (
        ('female', '女性'),
        ('male', '男性'),
        ('not_specified', '未回答'),
    )
    
    full_name = forms.CharField(label='お名前') 
    furigana = forms.CharField(label='フリガナ')
    postal_code = forms.CharField(label='郵便番号')
    prefecture = forms.CharField(label='都道府県')
    city = forms.CharField(label='市区町村', max_length=20)
    street_address = forms.CharField(label='番地')
    building_name = forms.CharField(label='建物名')
    telephone_number = forms.CharField(label='電話番号')
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    date_of_birth = forms.DateField(label='生年月日')
    privacy_policy_agreement = forms.BooleanField(label='プライバシーポリシーに同意する', required=True)

    class Meta:
        model = User
        fields = ("username",  "full_name", "furigana", "postal_code", "prefecture", "city", "street_address", "building_name", "telephone_number", "gender", "date_of_birth", "privacy_policy_agreement")

class SignupForm(UserCreationForm):
    """ユーザー登録確認用フォーム"""
    GENDER_CHOICES = (
        ('female', '女性'),
        ('male', '男性'),
        ('not_specified', '未回答'),
    )
    
    full_name = forms.CharField(label='お名前') 
    furigana = forms.CharField(label='フリガナ')
    postal_code = forms.CharField(label='郵便番号')
    prefecture = forms.CharField(label='都道府県')
    city = forms.CharField(label='市区町村', max_length=20)
    street_address = forms.CharField(label='番地')
    building_name = forms.CharField(label='建物名')
    telephone_number = forms.CharField(label='電話番号')
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    date_of_birth = forms.DateField(label='生年月日')
    privacy_policy_agreement = forms.BooleanField(label='プライバシーポリシーに同意する', required=True)

    class Meta:
        model = User
        fields = ("username",  "full_name", "furigana", "postal_code", "prefecture", "city", "street_address", "building_name", "telephone_number", "gender", "date_of_birth", "privacy_policy_agreement")

class CompleteForm(AuthenticationForm):
    pass

class LoginForm(AuthenticationForm):
    pass
    # 継承のみ
    