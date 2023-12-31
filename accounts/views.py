from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm, LoginForm, InputForm, CompleteForm, ResetForm 

class Input(generic.CreateView):
    form_class = InputForm
    template_name = "accounts/input.html"
    
    def get_success_url(self):
        # items:index のURL を逆引きして利用
        return reverse_lazy("account:sing_up") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 以下で、 辞書データ context に値を追加
        context["title"] = "新規お客様情報登録"
        return context
    

class SignUp(generic.CreateView):
    form_class = SignupForm # 利用するフォームクラスを設定
    template_name = "accounts/sign_up.html"
 
    def get_success_url(self):
        # items:index のURL を逆引きして利用
        return reverse_lazy("account:complete") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 以下で、 辞書データ context に値を追加
        context["title"] = "入力確認画面"
        return context
        
class Complete(TemplateView):
    """登録完了ページ"""
    template_name = 'accounts/complete.html'
        
# ログイン
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'
 
# ログアウト
class Logout(LogoutView):
    template_name = "accounts/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログアウトしました"
        return context
        
# パスワード再設定手続き
class Resetting(TemplateView):
    template_name = "accounts/resetting.html"
    
    
# パスワード再設定
class Reset(generic.CreateView):
    form_class = ResetForm
    template_name = "accounts/reset.html"
    
    def get_success_url(self):
        # items:index のURL を逆引きして利用
        return reverse_lazy("account:login") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 以下で、 辞書データ context に値を追加
        context["title"] = "パスワード再設定"
        return context
        
# パスワード再設定完了
class Recomplete(TemplateView):
    """パスワード再設定完了ページ"""
    template_name = 'accounts/recomplete.html'
    
# ユーザープロフィール
class Detail(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "入力内容確認"
        return context
 
# ユーザープロフィールの更新
class Update(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "パスワード再設定手続き"
        return context

