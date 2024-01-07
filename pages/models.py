from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_fullwidth(value):
    if not re.match(r'^[^\x01-\x7E\xA1-\xDF]+$', value):
        raise ValidationError(
            _('全角文字のみを入力してください。'),
        )


class Contact(models.Model):
    CHOICES = [
        ('-----------', '-----------'),
        ('商品について', '商品について'),
        ('お届けについて', 'お届けについて'),
        ('商品返品について', '商品返品について'),
        ('その他', 'その他'),
    ]
    name = models.CharField("お名前", max_length=20, blank=False, validators=[validate_fullwidth])
    email = models.EmailField("メールアドレス", max_length=50, blank=False)
    title = models.CharField("お問合せ項目", max_length=20, choices=CHOICES, default='-----------')
    message = models.TextField("お問合せ内容", max_length=400, blank=False)
    create_date = models.DateField(auto_now_add=True)
    reply = models.BooleanField("対応ステータス", default=False)
    
    def __str__(self):
        return str(self.title)