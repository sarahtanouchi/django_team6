from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
# from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import get_user_model
from .models import Order, Order_detail, Destination
 
User = get_user_model()
 
class SignupForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    class Meta:
        model = User
        fields = ("username",)

class LoginForm(AuthenticationForm):
    pass
    # 継承のみ
    
class DateInput(forms.DateInput):
    input_type = 'date'
    
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
                    "rows": 5,
                }
                
            ), 
        }
        
class DestinationCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ("name",)
        