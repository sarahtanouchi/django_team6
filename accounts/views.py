from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_date


from .models import Order, Coupon, Destination, Order_detail
from items.models import Item, Cart
from .forms import SignupForm, LoginForm, OrderCreateForm, OrderConfirmationForm

# vv order confirm helper functions vv

def create_destination(data):
    destination_name = data.get("destination_name")
    destination_kana = data.get("destination_kana")
    destination_address = data.get("destination_address")
    
    destination_postalcode1 = data.get("destination_postalcode1")
    destination_postalcode2 = data.get("destination_postalcode2")
    full_postal_code = destination_postalcode1 + destination_postalcode2
    
    destination_tel = data.get("destination_tel")
    destination_tel2 = data.get("destination_tel2")
    destination_tel3 = data.get("destination_tel3")
    full_tel_number = destination_tel + destination_tel2 + destination_tel3
    
    new_destination = Destination(name=destination_name, 
                                  kana=destination_kana, 
                                  address=destination_address, 
                                  postal_code=full_postal_code,
                                  tel_number=full_tel_number)

    return new_destination

def create_order(user, data):
    print(data)
    
    new_order = Order()
    new_order.user = user
    gift_wrapping_data = data.get("gift_wrapping")
    if gift_wrapping_data == "True":
        new_order.gift_wrapping = True
    
    arrival_request_data = data.get("arrival_request")
    if arrival_request_data == "True":
        arrival_date_data = data.get("arrival_date")
        new_order.arrival_date = parse_date(arrival_date_data)
    
    destination_choice = data.get("destination")
    if destination_choice == "user_address":
         new_order.destination = None # change this once user has destination field
         #new_order.destination = user.destination
    else:
        new_destination = create_destination(data)
        new_destination.save()
        new_order.destination = new_destination
        if destination_choice == "with_invoice":
            new_order.include_invoice = True
        elif destination_choice == "without_invoice":
            new_order.include_invoice = False

    coupon_code_data = data.get("couponcode")
    coupon_match = Coupon.objects.filter(code=coupon_code_data).first()
    if coupon_match is not None:
        new_order.coupon = coupon_match
        
    request_comment_data = data.get("request_comment")
    new_order.request_comment = request_comment_data
    
    return new_order
        
def create_order_detail(carts, order):
    
    new_order_detail = Order_detail()
    # new_order_detail.user = get_user_model()
    new_order_detail.user = order.user
    for cart in carts:
        pass
        new_order_detail.item = cart.item 
        new_order_detail.amount = cart.amount
        new_order_detail.price = cart.item.price
    
    return new_order_detail

# ^^ order confirm helper functions ^^

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
    
class OrderConfirmation(LoginRequiredMixin, generic.CreateView):
    template_name = "accounts/order_confirmation.html"
    form_class = OrderConfirmationForm # 必要ないかも?
    
    def show_confirm_form(self, request, *args, **kwargs):
        carts = self.request.user.cart_set.all()
        form = None
        if self.form_class is not None:
            form = self.form_class(request.POST)
        
        if request.POST:                
            return render(request, self.template_name, {"form": form, "order_data": request.POST, "carts": carts})
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        
    def save_order(self, request):
        new_order = create_order(self.request.user, request.POST)
        print()
        print("作成されたオーダー:")
        print(new_order)
        new_order.save() 
        
        carts = self.request.user.cart_set.all()
        new_order_detail = create_order_detail(carts, new_order)
        new_order.save()
        
        carts.delete()
        
    def post(self, request, *args, **kwargs):
        if "confirmed" in request.POST:
            
            self.save_order(request)
            return redirect("accounts:succeed_order")
        else:
            return self.show_confirm_form(request, *args, **kwargs)
            
class SucceedOrder(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/complete_order.html"

