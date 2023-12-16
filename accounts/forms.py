from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model
from .models import Order, Order_detail
 
User = get_user_model()
 
class SignupForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    class Meta:
        model = User
        fields = ("username",)

class LoginForm(AuthenticationForm):
    pass
    # 継承のみ
    
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("coupon","destination","arrival_date","gift_wrapping","request_comment",)
        widgets = {
            # "coupon":forms.Textarea(attrs={'cols':20}),
            # 'destinations':forms.CheckboxSelectMultiple()
        }