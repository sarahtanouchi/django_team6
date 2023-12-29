from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Avg

from .models import Item, Cart, Area, Item_type, Occasion, Tea_set_type, Tea_type, Taste, Flavor, Image, Review, Favorite, Information
from .forms import CartUpdateForm, ItemCreateForm, AreaCreateForm, ItemTypeCreateForm, OccasionCreateForm, TeaSetTypeCreateForm, TeaTypeCreateForm, TasteCreateForm, FlavorCreateForm, ImageCreateForm, ReviewForm, FavoriteAddForm, InformationCreateForm


# class Index(generic.ListView):
#     template_name = "items/index.html"
#     # 追記
#     model = Item
#     ordering = "-create_date"
 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "トップ"
#         return context

class Admin(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/admin.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "管理ページ"
        return context

class Item_management(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/item_management.html"
    def get_context_data(self, **kwargs):
        items = Item.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "商品管理ページ"
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
    success_url = reverse_lazy("items:admin")
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
    ordering = "-create_date"
    paginate_by = 4
    
    def get_queryset(self):
        item_type_filters = self.request.GET.getlist("item_type_filter", ["all"])
        tea_type_filters = self.request.GET.getlist("tea_type_filter", ["all"])
        tea_set_type_filters = self.request.GET.getlist("tea_set_type_filter", ["all"])
        price_filters = self.request.GET.getlist("price_filter", ["all"])
        taste_filters = self.request.GET.getlist("taste_filter", ["all"])
        occasion_filters = self.request.GET.getlist("occasion_filter", ["all"])
        items = Item.objects.all()
        if "all" not in tea_type_filters:
            items = items.filter(tea_type__name__in=tea_type_filters)
        if "all" not in tea_set_type_filters:
            items = items.filter(tea_set_type__name__in=tea_set_type_filters)
        if "all" not in item_type_filters:
            items = items.filter(item_type__name__in=item_type_filters)
        if "less_than_1000" in price_filters:
            items = items.filter(price__lte=1000)
        if "less_than_5000" in price_filters:
            items = items.filter(price__lte=5000)
        if "more_than_5000" in price_filters:
            items = items.filter(price__gte=5000)
        if "all" not in taste_filters:
            items = items.filter(taste__name__in=taste_filters)
        if "all" not in occasion_filters:
            items = items.filter(occasion__name__in=occasion_filters)
        
        return items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tea_types"] = Tea_type.objects.all()
        context["tea_set_types"] = Tea_set_type.objects.all()
        context["tastes"] = Taste.objects.all()
        context["occasions"] = Occasion.objects.all()
        # tea_type_filters = self.request.GET.getlist("tea_type_filter", ["all"])
        # context['tea_type_filters'] = tea_type_filters
        recommended_items = Item.objects.filter(recommended=True)
        context["recommended_items"] = recommended_items
        
        return context

class Item_detail(generic.DetailView):
    model = Item
    template_name = "items/item_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品詳細"
        # reviews = self.request.item.review_set.all()
        # context["reviews"] = reviews
        return context

@login_required        
def add_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    cart_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    
    cart_amount = int(request.POST["amount"])
    
    if created:
        cart_item.amount = cart_amount
    else:
        cart_item.amount += cart_amount
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
        context["title"] = "カートに入っている商品"
        carts = self.request.user.cart_set.all()
        context["carts"] = carts
        total = 0
        for cart in carts:
            total += cart.total_amount()
        context["total"] = total
        
        return context

# @login_required            
# def remove_cart_item(request, item_pk):
#     item = get_object_or_404(Item, pk=item_pk)
#     cart_item, created = Cart.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
    
#     if created == False:
#         cart_item.delete()
        
#     return redirect("items:carts")
        
class Delete_cart(LoginRequiredMixin, generic.DeleteView):
    model = Cart
    success_url = reverse_lazy("items:carts")
    
@login_required        
def update_amount(request,pk):
    item = get_object_or_404(Item, pk=pk)
    cart_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    
    cart_amount = int(request.POST["amount"])
    
    cart_item.amount = cart_amount

    cart_item.save()
    
    return redirect("items:carts")
   
        # # キーワード検索
        # keyword = self.request.GET.get('keyword', '')
        # if keyword:
        #     items = Item.objects.filter(
        #         Q(name__icontains=keyword) |
        #         Q(description__icontains=keyword) |
        #         Q(tags__name__icontains=keyword)
        #     )


# 新着情報管理        
class Information_list(LoginRequiredMixin, generic.ListView):
    model = Information
    template_name = "items/information_list.html"
    ordering = "-create_date"
    
    def get_queryset(self):
        return Information.objects.all()
    
    def get_context_data(self, **kwargs):
        information = Information.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "インフォメーション管理"
        return context
        
class Information_create(LoginRequiredMixin, generic.CreateView):
    model = Information
    template_name = "items/information_create.html"
    form_class = InformationCreateForm
    success_url = reverse_lazy("items:information_list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "インフォメーションの新規追加"
        return context
        
    # def form_valid(self, form):
    #     information = form.save(commit=False)
    #     information.save()
    #     return redirect("items:information_list")
        
class Information_update(LoginRequiredMixin, generic.UpdateView):
    model = Information
    template_name = "items/information_update.html"
    form_class = InformationCreateForm
    success_url = reverse_lazy("items:information_list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "インフォメーションの編集"
        return context
        
    # def form_valid(self, form):
    #     information = form.save(commit=False)
    #     information.save()
    #     return redirect("items:information_list")
        
class Information_delete(LoginRequiredMixin, generic.DeleteView):
    model = Information
    success_url = reverse_lazy("items:information_list")
    
# レビュー 
class Review_create(LoginRequiredMixin, generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'items/review_create.html'
    ordering = "-created_at"
    success_url = reverse_lazy("items:item_detail")
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "レビュー投稿"
        return context
        
    def form_valid(self, form):
        item_id = self.kwargs["pk"]
        item = get_object_or_404(Item, pk=item_id)
        review = form.save(commit=False)
        review.user = self.request.user
        review.item = item
        review.save() 
        
        return super().form_valid(form)
 
class Review_history(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = "items/review_history.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "レビュー投稿履歴"
        reviews = self.request.user.review_set.all()
        context["reviews"] = reviews
        return context
 
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class Favorite_list(LoginRequiredMixin, generic.ListView):
    model = Favorite
    form_class = FavoriteAddForm
    template_name = "items/favorite_list.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
        
class Recommend_item_list(generic.ListView):
    template_name = "pages/home.html"
    model = Item
    ordering = "-create_date"
    
    def get_queryset(self):
        item_type_filters = self.request.GET.getlist("item_type_filter", ["all"])
        tea_type_filters = self.request.GET.getlist("tea_type_filter", ["all"])
        tea_set_type_filters = self.request.GET.getlist("tea_set_type_filter", ["all"])
        price_filters = self.request.GET.getlist("price_filter", ["all"])
        taste_filters = self.request.GET.getlist("taste_filter", ["all"])
        occasion_filters = self.request.GET.getlist("occasion_filter", ["all"])
        items = Item.objects.all()
        if "all" not in tea_type_filters:
            items = items.filter(tea_type__name__in=tea_type_filters)
        if "all" not in tea_set_type_filters:
            items = items.filter(tea_set_type__name__in=tea_set_type_filters)
        if "all" not in item_type_filters:
            items = items.filter(item_type__name__in=item_type_filters)
        if "less_than_1000" in price_filters:
            items = items.filter(price__lte=1000)
        if "less_than_5000" in price_filters:
            items = items.filter(price__lte=5000)
        if "more_than_5000" in price_filters:
            items = items.filter(price__gte=5000)
        if "all" not in taste_filters:
            items = items.filter(taste__name__in=taste_filters)
        if "all" not in occasion_filters:
            items = items.filter(occasion__name__in=occasion_filters)
        
        return items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tea_types"] = Tea_type.objects.all()
        context["tea_set_types"] = Tea_set_type.objects.all()
        context["tastes"] = Taste.objects.all()
        context["occasions"] = Occasion.objects.all()

        return context
        