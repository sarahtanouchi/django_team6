from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_date
from django.http import HttpResponseRedirect
from .models import Order, Destination, Order_detail
from items.models import Item, Cart, Coupon
from .forms import SignupForm, LoginForm, OrderCreateForm, OrderConfirmationForm

User = get_user_model()

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
    print("マッチしたクーポン")
    print("coupon code:", coupon_code_data)
    print("db object:", coupon_match)
    if coupon_match is not None:
        new_order.coupon = coupon_match
        
    request_comment_data = data.get("request_comment")
    new_order.request_comment = request_comment_data
    
    return new_order
        
def create_order_details(carts, order):
    
    for cart in carts:
        new_order_details = Order_detail()
        new_order_details.order = order
        new_order_details.item = cart.item 
        new_order_details.amount = cart.amount
        new_order_details.purchase_price = cart.item.price
        new_order_details.save()

# ^^ order confirm helper functions ^^

class SignUp(generic.CreateView):
    model = User
    form_class = SignupForm # 利用するフォームクラスを設定
    template_name = "accounts/sign_up.html"
    success_url = reverse_lazy('accounts:complete')
 
    # def get_success_url(self):
    #     # items:index のURL を逆引きして利用
    #     return reverse_lazy("accounts:complete") 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新規お客様情報登録"
        return context
        
    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'accounts/signup_confirmation.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'accounts/sign_up.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        # else:
        #     # 正常動作ではここは通らない。エラーページへの遷移でも良い
        #     return redirect(reverse_lazy('home'))
        
class Complete(generic.TemplateView):
    """登録完了ページ"""
    template_name = 'accounts/complete_signup.html'
        
# ログイン
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'
 
# ログアウト
# class Logout(LogoutView):
#     template_name = "accounts/logout.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "ログアウトしました"
#         return context

class Logout(LogoutView):

    def get(self, request, *args, **kwargs):
        context = {'title': 'ログアウトしました'}
        return render(request, 'accounts/logout.html', context)
        
    def post(self, request, *args, **kwargs):
        # ログアウト処理が完了した後、accounts/login にリダイレクト
        response = super().post(request, *args, **kwargs)
        if request.is_ajax():
            return response
        print("Redirecting to login page...")
        return redirect('login')

# # パスワード再設定手続き
# class Resetting(TemplateView):
#     template_name = "accounts/resetting.html"
    
    
# # パスワード再設定
# class Reset(generic.CreateView):
#     form_class = ResetForm
#     template_name = "accounts/reset.html"
    
#     def get_success_url(self):
#         # items:index のURL を逆引きして利用
#         return reverse_lazy("account:login") 
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # 以下で、 辞書データ context に値を追加
#         context["title"] = "パスワード再設定"
#         return context
        
# # パスワード再設定完了
# class Recomplete(TemplateView):
#     """パスワード再設定完了ページ"""
#     template_name = 'accounts/recomplete.html'
    
# ユーザープロフィール
class Detail(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お客様情報"
        return context
 
# ユーザープロフィールの更新
class Update(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お客さ様情報の変更"
        return context

class Mypage(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/mypage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "マイページ"
        # context["user_pk"] = self.request.user.pk  # ユーザー主キーを取得してコンテキストに追加
        return context

class Order_create(LoginRequiredMixin, generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "accounts/orders.html"
    context_object_name = 'profile_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ご注文ページ"
        carts = self.request.user.cart_set.all()
        context["carts"] = carts
        subtotal8_with_tax = 0
        subtotal10_with_tax = 0
        for cart in carts:
            if cart.item.tax_percent == 8:
                subtotal8_with_tax += cart.total_amount()
            elif cart.item.tax_percent == 10:
                subtotal10_with_tax += cart.total_amount()
                
        context["subtotal8_with_tax"] = subtotal8_with_tax
        context["subtotal10_with_tax"] = subtotal10_with_tax
        
        tax8 = round(subtotal8_with_tax*0.08/1.08) 
        tax10 = round(subtotal10_with_tax*0.1/1.1) 
        
        context["tax8"] = tax8
        context["tax10"] = tax10
        
        subtotal8 = subtotal8_with_tax - tax8
        subtotal10 = subtotal10_with_tax - tax10
        
        context["subtotal8"] = subtotal8
        context["subtotal10"] = subtotal10
        
        total = 0
        for cart in carts:
            total += cart.total_amount()
            
        context["total"] = total
        return context
        
    def form_valid(self, form):
        order = form.save(commit=False)
        print(self.request.POST)
        # order.save()
        return redirect("account:order_confirmation")
    
class Order_confirmation(LoginRequiredMixin, generic.CreateView):
    template_name = "accounts/order_confirmation.html"
    form_class = OrderConfirmationForm # 必要ないかも?
    
    def show_confirm_form(self, request, *args, **kwargs):
        carts = self.request.user.cart_set.all()
        form = None
        
        if self.form_class is not None:
            form = self.form_class(request.POST)
            
        subtotal8_with_tax = 0
        subtotal10_with_tax = 0
        for cart in carts:
            if cart.item.tax_percent == 8:
                subtotal8_with_tax += cart.total_amount()
            elif cart.item.tax_percent == 10:
                subtotal10_with_tax += cart.total_amount()  
                
        tax8 = round(subtotal8_with_tax*0.08/1.08) 
        tax10 = round(subtotal10_with_tax*0.1/1.1) 
        
        subtotal8 = subtotal8_with_tax - tax8
        subtotal10 = subtotal10_with_tax - tax10
        
        discount8 = 0
        discount10 = 0
        # tax_discount8 = 0
        # tax_discount10 = 0

        coupon_code = self.request.POST.get('couponcode')
        coupon_match = Coupon.objects.filter(code=coupon_code).first()
        if coupon_match:
            discount8 = subtotal8 * coupon_match.discount_percent/100
            discount10 = subtotal10 * coupon_match.discount_percent/100
            # tax_discount8 = tax8 * coupon_match.discount_percent/100
            # tax_discount10 = tax10 * coupon_match.discount_percent/100

        
        discounted_subtotal8 = round(subtotal8 - discount8)
        discounted_subtotal10 = round(subtotal10 - discount10)
        
        # discounted_tax8 = round(tax8 - tax_discount8)
        # discounted_tax10 = round(tax10 - tax_discount10)
        tax_discount8 = round(discounted_subtotal8*0.08)
        tax_discount10 = round(discounted_subtotal10*0.1)
        
        # discount8 = subtotal8 * coupon.discount_percentage/100
        # discount10 = subtotal8 * coupon.discount_percentage/100
    
        # discounted_tax8 = tax8 - tax_discount8
        # discounted_tax10 = tax10 - tax_discount10
        
        discounted_subtotal8_with_tax = round(discounted_subtotal8 + tax_discount8)
        discounted_subtotal10_with_tax = round(discounted_subtotal10 + tax_discount10)
        
        discounted_total = discounted_subtotal8_with_tax + discounted_subtotal10_with_tax
        
        total = 0
        for cart in carts:
            total += cart.total_amount()

            
        context = {}
        if request.POST:
            context["order_data"] = request.POST
            context["form"] = form
            # return render(request, self.template_name, {"form": form, "order_data": request.POST, "carts": carts})
        else:
            context = self.get_context_data(**kwargs)
        
        context["title"] = "注文内容確認ページ" 
        context["carts"] = carts
        context["coupon_code"] = coupon_match
        context["subtotal8_with_tax"] = subtotal8_with_tax
        context["subtotal10_with_tax"] = subtotal10_with_tax
        context["tax8"] = tax8
        context["tax10"] = tax10
        context["subtotal8"] = subtotal8
        context["subtotal10"] = subtotal10
        context["total"] = total
        context["discounted_subtotal8"] = discounted_subtotal8
        context["discounted_subtotal10"] = discounted_subtotal10
        # context["discounted_tax8"] = discounted_tax8
        # context["discounted_tax10"] = discounted_tax10
        context["tax_discount8"] = tax_discount8
        context["tax_discount10"] = tax_discount10
        context["discounted_subtotal8_with_tax"] = discounted_subtotal8_with_tax
        context["discounted_subtotal10_with_tax"] = discounted_subtotal10_with_tax
        context["discounted_total"] = discounted_total
        
        return self.render_to_response(context)
        
    def save_order(self, request):
        new_order = create_order(self.request.user, request.POST)
        print()
        print("作成されたオーダー:")
        print(new_order)
        new_order.save() 
        
        carts = self.request.user.cart_set.all()
        create_order_details(carts, new_order)

        carts.delete()
        
    def post(self, request, *args, **kwargs):
        if "confirmed" in request.POST:
            
            self.save_order(request)
            return redirect("accounts:succeed_order")
        else:
            return self.show_confirm_form(request, *args, **kwargs)
            
class Succeed_order(LoginRequiredMixin, generic.TemplateView):
    template_name = "accounts/complete_order.html"
    
class Order_history(LoginRequiredMixin, generic.ListView):
    model=Order
    template_name = "accounts/order_history.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ご購入履歴"
        orders = self.request.user.order_set.all()
        
        orders_with_details = []
        for order in orders:
            total = 0
            order_details = order.order_detail_set.all()
            for order_detail in order_details:
                total += order_detail.purchase_price*order_detail.amount
        
            order_information = {
                "order": order,
                "order_details": order_details,
                "total": total
            }
            
            orders_with_details.append(order_information)
            
        # context["orders"] = orders
        # order_details = Order_detail.objects.all()
        # order_details = self.order.order_detail_set.all()
        context["order_history"] = orders_with_details
        
        return context
        
class Order_details(generic.DetailView):
    model = Order
    template_name = "accounts/order_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ご注文の詳細"
        print(context)
        order = context["order"]
        order_details = order.order_detail_set.all()
        context["order_details"] = order_details 
        
        subtotal8_with_tax = 0
        subtotal10_with_tax = 0
        for order_detail in order_details:
            if order_detail.item.tax_percent == 8:
                subtotal8_with_tax += order_detail.total_amount()
            elif order_detail.item.tax_percent == 10:
                subtotal10_with_tax += order_detail.total_amount()  
                
        tax8 = round(subtotal8_with_tax*0.08/1.08) 
        tax10 = round(subtotal10_with_tax*0.1/1.1) 
        
        subtotal8 = subtotal8_with_tax - tax8
        subtotal10 = subtotal10_with_tax - tax10
        
        discount8 = 0
        discount10 = 0
        
        if order.coupon :
            discount8 = subtotal8 * order.coupon.discount_percent/100
            discount10 = subtotal10 * order.coupon.discount_percent/100

        discounted_subtotal8 = round(subtotal8 - discount8)
        discounted_subtotal10 = round(subtotal10 - discount10)
        
        tax_discount8 = round(discounted_subtotal8*0.08)
        tax_discount10 = round(discounted_subtotal10*0.1)
        
        discounted_subtotal8_with_tax = round(discounted_subtotal8 + tax_discount8)
        discounted_subtotal10_with_tax = round(discounted_subtotal10 + tax_discount10)
        
        discounted_total = discounted_subtotal8_with_tax + discounted_subtotal10_with_tax
 
        
        total = 0
        for order_detail in order_details:
            total += order_detail.total_amount()
            
        context["total"] = total
        context["subtotal8_with_tax"] = subtotal8_with_tax
        context["subtotal10_with_tax"] = subtotal10_with_tax
        context["tax8"] = tax8
        context["tax10"] = tax10
        context["subtotal8"] = subtotal8
        context["subtotal10"] = subtotal10
        context["total"] = total
        context["discounted_subtotal8"] = discounted_subtotal8
        context["discounted_subtotal10"] = discounted_subtotal10
        context["tax_discount8"] = tax_discount8
        context["tax_discount10"] = tax_discount10
        context["discounted_subtotal8_with_tax"] = discounted_subtotal8_with_tax
        context["discounted_subtotal10_with_tax"] = discounted_subtotal10_with_tax
        context["discounted_total"] = discounted_total
        
        return context
        
   
    
