from django.db import models
from django.conf import settings
 
from django.contrib.auth import get_user_model
 
from accounts.models import User

class Item_type(models.Model):
    name = models.CharField("商品タイプ名", max_length=200)

class Occasion(models.Model):
    name = models.CharField("利用場面名", max_length=200)
    
class Tea_type(models.Model):
    name = models.CharField("お茶の種類名", max_length=200)
    
class Taste(models.Model):
    name = models.CharField("テイスト名", max_length=200)
    
class Area(models.Model):
    name = models.CharField("生産地名", max_length=200)
    description = models.CharField("詳細情報", max_length=1000, blank=True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField("商品名", max_length=200)
    price = models.PositiveIntegerField("価格")
    status = models.BooleanField("公開フラグ", default=True)
    stock = models.PositiveIntegerField("在庫数")
    description = models.CharField("商品詳細", max_length=1000)
    item_type = models.ForeignKey(Item_type, on_delete=models.CASCADE, verbose_name="カテゴリー")
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    tea_type = models.ForeignKey(Tea_type, on_delete=models.CASCADE, blank=True)
    taste = models.ForeignKey(Taste, on_delete=models.CASCADE, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    image = models.ImageField("画像", blank=True)
    second_image = models.ImageField("画像2", blank=True)
    cart_users = models.ManyToManyField(get_user_model(), related_name="cart_items", through="Cart")
    create_date = models.DateTimeField("作成日", auto_now_add=True)
    update_date = models.DateTimeField("更新日", auto_now=True)
    
    def __str__(self):
        return self.name
      
class Image(models.Model):
    image = models.ImageField("画像")

class Item_image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
  
    
class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField("評価")
    comment = models.CharField("コメント", max_length=200, blank=True)
    create_date = models.DateTimeField("投稿日", auto_now_add=True)
    update_date = models.DateTimeField("更新日", auto_now=True, blank=True)
    
class Cart(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("購入数", )
    
    class Meta:
        unique_together = ('item', 'user')
    
    def total_amount(self):
        return self.item.price * self.amount