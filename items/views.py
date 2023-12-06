from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Item, Cart, Area, Item_type, Occasion, Tea_set_type, Tea_type, Taste, Flavor, Image
from .forms import CartUpdateForm, ItemCreateForm, AreaCreateForm, ItemTypeCreateForm, OccasionCreateForm, TeaSetTypeCreateForm, TeaTypeCreateForm, TasteCreateForm, FlavorCreateForm, ImageCreateForm

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
        
class Create_item_type(LoginRequiredMixin, generic.CreateView):
    model = Item_type
    form_class = ItemTypeCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品タイプ登録"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_item_type")

class Create_occasion(LoginRequiredMixin, generic.CreateView):
    model = Occasion
    form_class = OccasionCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "利用シーン登録"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_occasion")

class Create_tea_set_type(LoginRequiredMixin, generic.CreateView):
    model = Tea_set_type
    form_class = TeaSetTypeCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "茶器タイプ登録"
        return context
    
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_tea_set_type")
               
class Create_tea_type(LoginRequiredMixin, generic.CreateView):
    model = Tea_type
    form_class = TeaTypeCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お茶タイプ登録"
        return context
    
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_tea_type")
        
class Create_taste(LoginRequiredMixin, generic.CreateView):
    model = Taste
    form_class = TasteCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "テイスト登録"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_taste")
        
class Create_flavor(LoginRequiredMixin, generic.CreateView):
    model = Flavor
    form_class = FlavorCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "風味登録"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_flavor")
        
class Create_area(LoginRequiredMixin, generic.CreateView):
    model = Area
    form_class = AreaCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "エリア登録"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_area")
        
class Create_image(LoginRequiredMixin, generic.CreateView):
    model = Image
    form_class = ImageCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "画像登録"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_image")
        
class Image_list(generic.ListView):
    model = Image
    
    template_name = "items/image_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "画像の編集"
        return context
        
class Image_update(LoginRequiredMixin, generic.UpdateView):
    model = Image
    form_class = ImageCreateForm
    success_url = reverse_lazy("items:image_list")
    template_name = "items/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "画像の編集"
        return context

class Delete_image(LoginRequiredMixin, generic.DeleteView):
    model = Image
    success_url = reverse_lazy("items:image_list")
 
class Create(LoginRequiredMixin, generic.CreateView):
    model = Item
    form_class = ItemCreateForm
    success_url = reverse_lazy("items:admin")
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品の新規登録"
        return context
    
    # def form_valid(self, form):
    #     item = form.save(commit=False)
    #     item.save()
    #     return redirect("items:admin")
 
        
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
    
class Item_list(generic.ListView):
    template_name = "items/item_list.html"
    model = Item
    # ordering = "-create_date"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Item_detail(generic.DetailView):
    model = Item
    template_name = "items/item_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品詳細"
        return context

@login_required        
def add_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    cart_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    if created:
        cart_item.amount = 1
    else:
        cart_item.amount += 1
    cart_item.save()
    
    
    # cart_records = Cart.objects.filter(user=request.user, ordered=False)
    
    # if cart_records.exists():
    #     cart = cart[0]
    #     if cart.items.filter(item_pk=item.pk).exists():
    #         cart.quantity += 1
    #         cart.save()
    #     else:
    #         cart.items.add(cart_item)
    # else:
    #     cart = Cart.objects.create(user=request.user, item=)
    #     cart.items.add(cart_item)
        
    return redirect("items:carts")
            
    
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
        
    
    