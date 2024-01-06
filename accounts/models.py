from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="メールアドレス", max_length=255, unique=True)
    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"
    
    GENDER_CHOICES = (
        ('female', '女性'),
        ('male', '男性'),
        ('not_specified', '未回答'),
    )
    
    name = models.CharField(verbose_name='お名前', max_length=50, null=True) 
    kana = models.CharField(verbose_name='フリガナ', max_length=50, null=True)
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ('正しい郵便番号を入力してください。'))
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号', null=True)
    # postal_code = models.CharField(verbose_name='郵便番号', max_length=20, validators=[RegexValidator(r'^\d{7}$', message='正しい郵便番号を入力してください。')])
    prefecture = models.CharField(verbose_name='都道府県', max_length=50, null=True)
    city = models.CharField(verbose_name='市区町村', max_length=50, null=True)
    street_address = models.CharField(verbose_name='番地', max_length=100, null=True)
    building_name = models.CharField(verbose_name='建物名', max_length=100, blank=True, null=True)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ('正しい電話番号を入力してください。'))
    tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号', null=True)
    # tel_number = models.CharField(verbose_name='電話番号', max_length=20, validators=[RegexValidator(r'^\d{8,}$', message='正しい電話番号を入力してください。')])
    gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=20, null=True)
    birthdate = models.DateField(verbose_name='生年月日', blank= True, null=True)
    privacy_policy_agreement = models.BooleanField(verbose_name='プライバシーポリシーに同意', default=False)
    create_date = models.DateTimeField(verbose_name='作成日', auto_now_add=True, null=True)
    
    def get_username(self):
        return self.username

# class User(models.Model):
#     email = models.EmailField("メールアドレス")
#     password = models.CharField("パスワード", max_length=20)
#     username = models.CharField("ユーザー名", max_length=20)
#     name = models.CharField("名前", max_length=50)
#     kana = models.CharField("フリガナ", max_length=50)
#     postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
#     postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
    
from items.models import Item

class Destination(models.Model):
    name = models.CharField("名前", max_length=200)
    kana = models.CharField("フリガナ", max_length=200)
    postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ('正しい郵便番号を入力してください。'))
    postal_code = models.CharField("郵便番号",validators=[postal_code_regex], max_length=7) 
    address = models.CharField("住所", max_length=200)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ('正しい電話番号を入力してください。'))
    tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')


from items.models import Coupon

class Order(models.Model):
    ORDER_STATUS = (
        ("accepted","注文受付"),
        ("delivered","配達済み"),
        ("canceled","キャンセル済み"),
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)
    arrival_date = models.DateField("お届け日",blank=True, null=True)
    gift_wrapping = models.BooleanField("ギフトラッピング", default=False)
    request_comment = models.CharField("要望", max_length=1000, blank=True)
    include_invoice = models.BooleanField("レシート同封", default=True)
    status = models.CharField("注文ステータス", max_length=200, choices=ORDER_STATUS, default="accepted", null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, blank=True, null=True)
    purchase_date = models.DateTimeField("購入日", auto_now_add=True)
    update_date = models.DateTimeField("更新日", auto_now=True)
    
class Order_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField("購入数")
    purchase_price = models.PositiveIntegerField("購入価格")

