from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order
from items.models import Item
from .forms import SignupForm, LoginForm, OrderCreateForm, OrderConfirmationForm
 
class SignUp(generic.CreateView):
    form_class = SignupForm # 利用するフォームクラスを設定
    template_name = "accounts/sign_up.html"
 
    def get_success_url(self):
        # items:index のURL を逆引きして利用
        return reverse_lazy("items:index") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        # 以下で、 辞書データ context に値を追加
        context["title"] = "新規お客様情報登録"
 
        return context
        
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
 
# ユーザープロフィール
class Detail(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プロフィール"
        return context
 
# ユーザープロフィールの更新
class Update(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "プロフィール編集"
        return context

class Mypage(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/mypage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "マイページ"
        # context["user_pk"] = self.request.user.pk  # ユーザー主キーを取得してコンテキストに追加
        return context

class OrderCreate(LoginRequiredMixin, generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "accounts/orders.html"
    context_object_name = 'profile_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ご注文ページ"
        carts = self.request.user.cart_set.all()
        context["carts"] = carts
        # total = 0
        # for order in orders:
        #     total += order.total_amount()
        # context["total"] = total
        
        return context
        
    def form_valid(self, form):
        order = form.save(commit=False)
        print(self.request.POST)
        # order.save()
        return redirect("account:order_confirmation")
    
class OrderConfirmation(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/order_confirmation.html"
    form_class = OrderConfirmationForm # 必要ないかも?
    
    def post(self, request, *args, **kwargs):
        carts = self.request.user.cart_set.all()

        form = None
        if self.form_class is not None:
            form = self.form_class(request.POST)
            
        print(request.POST) # print post data in terminal
        
        if request.POST:                
            return render(request, self.template_name, {"form": form, "order_data": request.POST, "carts": carts})
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
