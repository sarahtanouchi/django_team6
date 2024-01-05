from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
# from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model
from .models import Order, Order_detail, Destination, CustomUser
 
User = get_user_model()
 
class DateInput(forms.DateInput):
    input_type = 'date'
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        
        fields = [
            "username",
            "name",
            "kana",
            "postal_code",
            "prefecture",
            "city",
            "street_address",
            "building_name",
            "tel_number",
            "gender",
            "birthdate",
            "email",
            "privacy_policy_agreement",
            # "password1",
            # "password2",
        ]
        
        error_messages = {
            'privacy_policy_agreemen': {
                'required': "アカウントの作成にはプライバシーポリシーへの同意が必要です。",
            },
        }
        
        widgets = {
            "birthdate": DateInput(),
            "username": forms.Textarea(
                attrs={
                    "placeholder":"※口コミ投稿に表示されます",
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "name": forms.Textarea(
                attrs={
                    "placeholder":"全角",
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "kana": forms.Textarea(
                attrs={
                    "placeholder":"全角カナ",
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "postal_code": forms.TextInput(
                attrs={
                    "cols": 30,
                    "rows": 1,
                }
            ), 
            "prefecture": forms.TextInput(
                attrs={
                    "cols": 30,
                    "rows": 1,
                }
            ), 
            "city": forms.Textarea(
                attrs={
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "street_address": forms.Textarea(
                attrs={
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "building_name": forms.Textarea(
                attrs={
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "tel_number": forms.Textarea(
                attrs={
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "email": forms.Textarea(
                attrs={
                    "placeholder":"半角英数字",
                    "cols": 50,
                    "rows": 1,
                }
            ), 
            "password1": forms.TextInput(
                attrs={
                    "placeholder":"半角英数字を混ぜた８〜１２文字",
                }
            ), 
            "password2": forms.TextInput(
                attrs={
                    "placeholder":"半角英数字を混ぜた８〜１２文字",
                }
            ), 
        }
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['privacy_policy_agreement'].required = True

class LoginForm(AuthenticationForm):
    pass
    # 継承のみ
    
    
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("coupon","include_invoice","destination","arrival_date","gift_wrapping","request_comment",)
        widgets = {
            # "coupon":forms.Textarea(attrs={'cols':20}),
            # 'destinations':forms.CheckboxSelectMultiple()
            "arrival_date": DateInput(),
            "request_comment": forms.Textarea(
                attrs={
                    "placeholder":"ご要望があればご入力ください",
                    "cols": 100,
                    "rows": 5
                }
                
            ), 
        }
        
class OrderConfirmationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("coupon","include_invoice","destination","arrival_date","gift_wrapping","request_comment",)
        widgets = {
            # "coupon":forms.Textarea(attrs={'cols':20}),
            # 'destinations':forms.CheckboxSelectMultiple()
            "arrival_date": DateInput(
                attrs={
                    "readonly": True,
                    "disabled": True,
                }),
            "request_comment": forms.Textarea(
                attrs={
                    "placeholder":"ご要望があればご入力ください",
                    "cols": 100,
                    "rows": 5,
                    "readonly": True,
                }
                
            ), 
        }
        
class DestinationCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ("name",)
        