from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="メールアドレス", max_length=255, unique=True)
    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"
    
    def get_username(self):
        return self.username
        
class User(models.Model):
    email = models.EmailField("メールアドレス")
    password = models.CharField("パスワード", max_length=20)
    username = models.CharField("ユーザー名", max_length=20)
    name = models.CharField("名前", max_length=50)
    kana = models.CharField("フリガナ", max_length=50)
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
    
class SignupForm(UserCreationForm):
    """ユーザー登録用フォーム"""
    GENDER_CHOICES = (
        ('female', '女性'),
        ('male', '男性'),
        ('not_specified', '未回答'),
    )
    
    full_name = models.CharField(label='お名前') 
    furigana = models.CharField(label='フリガナ')
    postal_code = models.CharField(label='郵便番号')
    prefecture = models.CharField(label='都道府県')
    city = models.CharField(label='市区町村', max_length=20)
    street_address = models.CharField(label='番地')
    building_name = models.CharField(label='建物名')
    telephone_number = models.CharField(label='電話番号')
    gender = models.ChoiceField(label='性別', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    date_of_birth = models.CharField(label='生年月日')
    privacy_policy_agreement = models.BooleanField(label='プライバシーポリシーに同意する', required=True)
    
    