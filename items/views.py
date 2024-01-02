from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.db.models import Avg
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest

from .models import Item, Cart, Area, Item_type, Occasion, Tea_set_type, Tea_type, Taste, Flavor, Image, Review, Favorite, Information, Coupon
from .forms import CartUpdateForm, ItemCreateForm, AreaCreateForm, ItemTypeCreateForm, OccasionCreateForm, TeaSetTypeCreateForm, TeaTypeCreateForm, TasteCreateForm, FlavorCreateForm
from .forms import ImageCreateForm, ReviewForm, InformationCreateForm, FavoriteAddForm, SearchForm, CouponCreateForm


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

class Item_management(LoginRequiredMixin, generic.ListView):
    model=Item
    template_name = "items/item_management.html"
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        items = Item.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "商品管理"
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
        context["title"] = "画像新規追加"
        return context
        
    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        return redirect("items:create_image")
        
class Image_list(generic.ListView):
    model = Image
    template_name = "items/image_list.html"
    paginate_by = 30 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "画像管理"
        return context
        
class Update_image(LoginRequiredMixin, generic.UpdateView):
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
        
# 商品検索
def item_list(request):
    items = Item.objects.all()
    item_search_form = ItemSearchForm()

    return render(request, 'item_list.html', {'items': items, 'item_search_form': item_search_form})

class Item_detail(generic.DetailView):
    model = Item
    template_name = "items/item_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品詳細"
        item = context["item"]
        tax = round(item.price*0.1/1.1) 
        context["tax"]=tax
        reviews = self.object.review_set.all()
        context["reviews"] = reviews      
        
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
        context["title"] = "お知らせ管理"
        return context
        
class Information_create(LoginRequiredMixin, generic.CreateView):
    model = Information
    template_name = "items/information_create.html"
    form_class = InformationCreateForm
    success_url = reverse_lazy("items:information_list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お知らせの新規追加"
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
        context["title"] = "お知らせの編集"
        return context
        
class Information_delete(LoginRequiredMixin, generic.DeleteView):
    model = Information
    success_url = reverse_lazy("items:information_list")
   
# レビュー 
class Review_create(LoginRequiredMixin, generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'items/review_create.html'
    ordering = "-created_date"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "レビュー投稿"
        item_id = self.kwargs["pk"]
        item = get_object_or_404(Item, pk=item_id)
        context["item"] = item
        
        return context
        
    def form_valid(self, form):
        item_id = self.kwargs["pk"]
        item = get_object_or_404(Item, pk=item_id)
        
        try:
            review = form.save(commit=False)
            review.user = self.request.user
            review.item = item
            review.save() 
        except IntegrityError:
            # 重複がある場合の処理
            return HttpResponseBadRequest("このアイテムに対するレビューは既に存在します。")
            
        return redirect("items:item_detail", pk=item_id)

#　商品ごとのレビュー        
class Review_list(generic.ListView):
    model = Review
    template_name = "items/item_detail.html"
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "レビュー"
        
      # 商品ごとのrate平均
        item_id = self.kwargs.get('pk')
        average_rate = Review.objects.filter(item__id=item_id).aggregate(Avg('rate'))['rate__avg']
        context["average_rate"] = average_rate
        return context
        
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(item=self.request.item)
        return queryset
        
        # item_id = self.kwargs.get('pk')
        # return queryset.filter(item__id=item_id)
        
# ユーザーのレビュー投稿履歴
class Review_history(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = "items/review_history.html"
    ordering = "-created_at"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "レビュー投稿履歴"
        reviews = self.request.user.review_set.all()
        context["reviews"] = reviews
        return context
 
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(user=self.request.user)
        return queryset

class Review_delete(LoginRequiredMixin, generic.DeleteView):
    model = Review
    success_url = reverse_lazy("items:review_history") 

# お気に入り
class Favorite_add(LoginRequiredMixin, generic.View):
    model = Favorite
    form_class = FavoriteAddForm
    
    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs['pk'])
        favorite, created = Favorite.objects.get_or_create(
            item=item,
            user=request.user,
        )
        favorite_item.save()

        return HttpResponse("お気に入りに追加しました。")

# @login_required        
# def add_favorite(request,pk):
#     item = get_object_or_404(Item, pk=pk)
#     favorite_item, created = Favorite.objects.get_or_create(
#         item=item,
#         user=request.user,
#     )
#     favorite_item.save()

class Favorite_list(LoginRequiredMixin, generic.ListView):
    model = Favorite
    template_name = "items/favorite_list.html"
    context_object_name = "favorite"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お気に入りリスト"
 
        return context
    
    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset

class Favorite_delete(LoginRequiredMixin, generic.DeleteView):
    model = Favorite
    success_url = reverse_lazy("items:favorite_list")
    


# キーワード検索
def item_search(request):
    form = SearchForm(request.GET)
    items = []

    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        items = Item.objects.filter(name__startswith=search_term)

    return render(request, 'item_list.html', {'items': items, 'item_search_form': form})
    
class Coupon_list(LoginRequiredMixin, generic.ListView):
    model = Coupon
    template_name = "items/coupon_list.html"
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "クーポン管理"
        return context

class Create_coupon(LoginRequiredMixin, generic.CreateView):
    model = Coupon
    form_class = CouponCreateForm
    template_name = "items/create.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "クーポン新規追加"
        return context
        
    def form_valid(self, form):
        coupon = form.save(commit=False)
        coupon.save()
        return redirect("items:coupon_list")
        
class Update_coupon(LoginRequiredMixin, generic.UpdateView):
    model = Coupon
    form_class = CouponCreateForm
    success_url = reverse_lazy("items:coupon_list")
    template_name = "items/update.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "クーポンの編集"
        return context

class Delete_coupon(LoginRequiredMixin, generic.DeleteView):
    model = Coupon
    success_url = reverse_lazy("items:coupon_list")