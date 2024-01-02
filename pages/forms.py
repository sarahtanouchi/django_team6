from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "title",
            "message",
        ]
    
    
    # name = forms.CharField(
    #     label='お名前',
    #     max_length=30,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "全角で入力して下さい",
    #     }),
    # )
    # email = forms.EmailField(
    #     label='メールアドレス',
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': "半角英数字で入力して下さい",
    #     }),
    # )
    CHOICES = [
        ('-----------', '-----------'),
        ('商品について', '商品について'),
        ('お届けについて', 'お届けについて'),
        ('商品返品について', '商品返品について'),
        ('その他', 'その他'),
    ]

    title = forms.ChoiceField(
        label='お問合せ項目',
        choices=CHOICES,
        initial='-----------',
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
    )
    
    message = forms.CharField(
        label='お問い合わせ内容',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "400文字以内で入力してください",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")