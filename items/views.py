from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Item, Cart
from .forms import CartUpdateForm

class Index(LoginRequiredMixin, generic.ListView):
    template_name = "items/index.html"
    # 追記
    model = Item
    ordering = "-created_at"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "トップ"
        return context
 
class Create(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品の新規登録"
        return context
 
class Detail(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品詳細"
        return context
 
class Update(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品情報の編集"
        return context
        
class Carts(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/carts.html"
    context_object_name = 'profile_user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "カート内の商品"
        carts = self.request.user.cart_set.all()
        context["carts"] = carts
        total = 0
        for cart in carts:
            total += cart.total_amount()
        context["total"] = total
        
        return context
        
def addCarts(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.user.cart_set.filter(item_id=item.id).exists():
        cart = request.user.cart_set.filter(item_id=item.id).get()
        cart.amount += 1
        cart.save()
        messages.success(request, f"{item.name}をカートに追加しました。カート内の数量: {cart.amount}")
    else:
        Cart(item=item, user=request.user, amount=1).save()
        messages.success(request, f"{item.name}をカートに追加しました。カート内の数量: 1")

    return redirect("items:index")
    
def update_cart(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    cart.amount = request.POST.get("amount")
    cart.save()
    return redirect("items:carts")
    
def purchase(request):
    carts = request.user.cart_set.all()
    for cart in carts:
        if cart.amount > cart.item.stock:
            messages.error(request, f"{cart.item.name}の在庫が足りません。購入可能数: {cart.item.stock}")
        else:
            cart.item.stock -= cart.amount
    print(len(messages.get_messages(request)))
    if len(messages.get_messages(request)) > 0:
        return redirect("items:index")
    
    for cart in carts:
        cart.item.save()
        
    for cart in carts:
        cart.delete()
        
    messages.success(request, "商品を購入しました。")
        
    return redirect("items:index")
    