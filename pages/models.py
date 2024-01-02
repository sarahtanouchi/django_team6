from django.db import models

class Contact(models.Model):
    CHOICES = [
        (1, '商品について'),
        (2, 'お届けについて'),
        (3, '商品返品について'),
        (4, 'その他'),
    ]
    name = models.CharField("お名前", max_length=30, blank=False)
    email = models.EmailField("メールアドレス", max_length=50, blank=False)
    title = models.BooleanField("お問合せ項目", default=0, choices=CHOICES)
    message = models.TextField("お問合せ内容", max_length=400, blank=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contacts'