from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Item, Cart, Area, Item_type, Occasion, Tea_type, Taste
from .forms import CartUpdateForm, ItemCreateForm, AreaCreateForm, ItemTypeCreateForm, OccasionCreateForm, TeaTypeForm, TasteForm

# class Index(LoginRequiredMixin, generic.ListView):
class Index(generic.ListView):
    template_name = "items/index.html"
    # 追記
    model = Item
    ordering = "-create_date"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "トップ"
        return context
        
class Admin(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/admin.html"
    def get_context_data(self, **kwargs):
        items = Item.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "管理ページ"
        context["items"] = items
        return context

class Create_area(LoginRequiredMixin, generic.CreateView):
    model = Area
    form_class = AreaCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "エリア登録"
        return context
        
class Create_item_type(LoginRequiredMixin, generic.CreateView):
    model = Item_type
    form_class = ItemTypeCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品タイプ登録"
        return context

class Create_occasion(LoginRequiredMixin, generic.CreateView):
    model = Occasion
    form_class = OccasionCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "エリア登録"
        return context
    
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:admin")
 
class Create(LoginRequiredMixin, generic.CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品の新規登録"
        return context
    
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:admin")
 
class Detail(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品詳細"
        return context
        
class Update(LoginRequiredMixin, generic.UpdateView):
    model = Item
    form_class = ItemCreateForm
    success_url = reverse_lazy("items:index")
    template_name = "items/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品情報の編集"
        return context
        
class Delete(LoginRequiredMixin, generic.DeleteView):
    model = Item
    success_url = reverse_lazy("items:admin")
        
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
    