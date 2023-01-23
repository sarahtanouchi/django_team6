from django.urls import path
from . import views
 
app_name = "items"
 
urlpatterns = [
    path("", views.Index.as_view(), name="index"), # 一覧
    path("create/", views.Create.as_view(), name="create"), # 新規作成
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # 詳細
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("add_carts/<int:pk>", views.addCarts, name="add_carts"),
    path("carts/", views.Carts.as_view(), name="carts"),
    path("purchase/", views.purchase, name="purchase"),
]