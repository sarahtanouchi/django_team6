from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    last_login = None

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
    postal_code = models.CharField("郵便番号", max_length=8)
    address = models.CharField("住所", max_length=200)
    tel_number = models.CharField("電話番号", max_length=11)


class Coupon(models.Model):
    code = models.CharField("クーポンコード", max_length=7)
    discount_percentage = models.PositiveIntegerField("割引率")


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)
    arrival_date = models.DateField("お届け日",blank=True)
    gift_wrapping = models.BooleanField("ギフトラッピング", default=False)
    request_comment = models.CharField("要望", max_length=1000)
    include_invoince = models.BooleanField("レシート同封", default=True)
    status = models.CharField("注文ステータス", max_length=200)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, blank=True, null=True)
    purchase_date = models.DateTimeField("購入日", auto_now_add=True)
    update_date = models.DateTimeField("更新日", auto_now=True)
    
class Order_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField("購入数")
    purchase_price = models.PositiveIntegerField("購入価格")
    



    
    
    