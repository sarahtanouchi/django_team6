from django.urls import path
from . import views
 
app_name = "items"
 
urlpatterns = [
    path("", views.Item_list.as_view(), name="index"), # 商品一覧画面
    path("admin/", views.Admin.as_view(), name="admin"), # 管理画面
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
    path("image_update/<int:pk>/", views.Image_update.as_view(), name="image_update"),
    path("delete_image/<int:pk>/", views.Delete_image.as_view(), name="delete_image"),
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("delete/<int:pk>/", views.Delete.as_view(), name="delete"),
    path("item_detail/<int:pk>/", views.Item_detail.as_view(), name="item_detail"), # 詳細
    path("add_item/<int:pk>/", views.add_item, name="add_item"),
    path("update_amount/<int:pk>/", views.update_amount, name="update_amount"),
    path("carts/", views.Carts.as_view(), name="carts"),
    # path("remove_cart_item/<int:item_pk>/", views.remove_cart_item, name="remove_cart_item"),
    path("delete_cart/<int:pk>/", views.Delete_cart.as_view(), name="delete_cart"),
    path("review_create/<int:pk>/", views.ReviewCreate.as_view(), name="review_create"), #レビュー投稿
    path("review_history/<int:pk>/", views.ReviewHistory.as_view(), name="review_history"), #ユーザーレビュー投稿履歴
    path("review_list/<int:pk>/", views.ReviewList.as_view(), name="review_list"), # 商品レビューリスト
    
]