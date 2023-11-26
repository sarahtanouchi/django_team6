from django.urls import path
from . import views
 
app_name = "items"
 
urlpatterns = [
    path("", views.Index.as_view(), name="index"), # 一覧
    path("admin/", views.Admin.as_view(), name="admin"), # 新規作成
    path("create/", views.Create.as_view(), name="create"), # 新規作成
    path("create_area/", views.Create_area.as_view(), name="create_area"), # 新規作成
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # 詳細
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("delete/<int:pk>/", views.Delete.as_view(), name="delete"), # 編集
    path("carts/", views.Carts.as_view(), name="carts"),
    
]