from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('female', '女性'),
        ('male', '男性'),
        ('not_specified', '未回答'),
    )
    
    full_name = models.CharField(verbose_name='お名前', max_length=100) 
    furigana = models.CharField(verbose_name='フリガナ', max_length=100)
    postal_code = models.CharField(verbose_name='郵便番号', max_length=20, validators=[RegexValidator(r'^\d{7}$', message='正しい郵便番号を入力してください。')])
    prefecture = models.CharField(verbose_name='都道府県', max_length=100)
    city = models.CharField(verbose_name='市区町村', max_length=50)
    street_address = models.CharField(verbose_name='番地', max_length=100)
    building_name = models.CharField(verbose_name='建物名', max_length=100)
    telephone_number = models.CharField(verbose_name='電話番号', max_length=20, validators=[RegexValidator(r'^\d{8,}$', message='正しい電話番号を入力してください。')])
    gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=20)
    date_of_birth = models.DateField(verbose_name='生年月日')
    privacy_policy_agreement = models.BooleanField(default=False)
    
    def get_username(self):
        return self.username

    pass
        
class User(models.Model):
    email = models.EmailField("メールアドレス", unique=True)
    password = models.CharField("パスワード", max_length=20)
    username = models.CharField("ユーザー名", max_length=20)
    name = models.CharField("名前", max_length=50)
    kana = models.CharField("フリガナ", max_length=50)
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
    
