from django.urls import path
from . import views
 
app_name = "items"
 
urlpatterns = [
    path("", views.Item_list.as_view(), name="index"), # 商品一覧画面
    path("admin/", views.Admin.as_view(), name="admin"), # 管理画面
    path("item_management/", views.Item_management.as_view(), name="item_management"),
    path("create/", views.Create.as_view(), name="create"), # 新規作成
    path("create_item_type/", views.Create_item_type.as_view(), name="create_item_type"),
    path("create_occasion/", views.Create_occasion.as_view(), name="create_occasion"),
    path("create_tea_set_type/", views.Create_tea_set_type.as_view(), name="create_tea_set_type"),
    path("create_tea_type/", views.Create_tea_type.as_view(), name="create_tea_type"),
    path("create_taste/",views.Create_taste.as_view(), name="create_taste"),
    path("create_flavor/",views.Create_flavor.as_view(), name="create_flavor"),
    path("create_area/", views.Create_area.as_view(), name="create_area"),
    path("create_image/", views.Create_image.as_view(), name="create_image"),
    path("image_list/", views.Image_list.as_view(), name="image_list"),
    path("update_image/<int:pk>/", views.Update_image.as_view(), name="update_image"),
    path("delete_image/<int:pk>/", views.Delete_image.as_view(), name="delete_image"),
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("delete/<int:pk>/", views.Delete.as_view(), name="delete"),
    path("item_detail/<int:pk>/", views.Item_detail.as_view(), name="item_detail"), # 詳細
    path("add_item/<int:pk>/", views.add_item, name="add_item"),
    path("update_amount/<int:pk>/", views.update_amount, name="update_amount"),
    path("carts/", views.Carts.as_view(), name="carts"),
    # path("remove_cart_item/<int:item_pk>/", views.remove_cart_item, name="remove_cart_item"),
    path("delete_cart/<int:pk>/", views.Delete_cart.as_view(), name="delete_cart"),
    path("information_list/", views.Information_list.as_view(), name="information_list"), # 新着情報管理
    path("information_create/", views.Information_create.as_view(), name="information_create"), # 新着情報新規作成
    path("information_update/<int:pk>/", views.Information_update.as_view(), name="information_update"), # 新着情報編集
    path("information_delete/<int:pk>/", views.Information_delete.as_view(), name="information_delete"), #新着情報削除
    path("review_create/<int:pk>/", views.Review_create.as_view(), name="review_create"), #レビュー投稿
    path("review_history/", views.Review_history.as_view(), name="review_history"), #ユーザーレビュー投稿履歴
    path("review_list/", views.Review_list.as_view(), name="review_list"), #各商品レビュー
    path("review_delete/<int:pk>/", views.Review_delete.as_view(), name="review_delete"), #レビュー投稿
    path("favorite_list/", views.Favorite_list.as_view(), name="favorite_list"), # お気に入りリスト
    path("favorite_add/<int:pk>/", views.Favorite_add.as_view(), name="favorite_add"), # お気に入り追加
    path("favorite_delete/<int:pk>/", views.Favorite_delete.as_view(), name="favorite_delete"), # お気に入り削除
    path("coupon_list/", views.Coupon_list.as_view(), name="coupon_list"),
    path("create_coupon/", views.Create_coupon.as_view(), name="create_coupon"),
    path("update_coupon/<int:pk>/", views.Update_coupon.as_view(), name="update_coupon"),
    path("delete_coupon/<int:pk>/", views.Delete_coupon.as_view(), name="delete_coupon"),
    path("coupon_info/", views.Coupon_info.as_view(), name="coupon_info"),
]