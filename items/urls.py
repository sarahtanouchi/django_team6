from django.urls import path
from . import views
 
app_name = "items"
 
urlpatterns = [
    path("", views.Index.as_view(), name="index"), # トップページ
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
    path("item_list/", views.Item_list.as_view(), name="item_list"),
    path("item_detail/<int:pk>/", views.Item_detail.as_view(), name="item_detail"), # 詳細
    path("add_item/", views.Add_item.as_view(), name="add_item"),
    path("carts/", views.Carts.as_view(), name="carts"),
    
]