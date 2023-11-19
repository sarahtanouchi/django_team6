from django.db import models
from django.conf import settings
 
from django.contrib.auth import get_user_model
 
class Category(models.Model):
    name = models.CharField("カテゴリー名", max_length=200)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField("商品名", max_length=200)
    description = models.CharField("説明", max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="カテゴリー")
    image = models.ImageField("画像", blank=True)
    second_image = models.ImageField("画像2", blank=True)
    price = models.PositiveIntegerField("価格", )
    stock = models.PositiveIntegerField("在庫数", )
    cart_users = models.ManyToManyField(get_user_model(), related_name="cart_items", through="Cart")
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("購入数", )
    
    class Meta:
        unique_together = ('item', 'user')
    
    def total_amount(self):
        return self.item.price * self.amount