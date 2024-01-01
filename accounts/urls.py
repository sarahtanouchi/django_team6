from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

 
app_name = "accounts"
 
urlpatterns = [
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),
    path("login/", views.Login.as_view(), name="login"), # ログイン
    path("logout/", views.Logout.as_view(), name="logout"), # ログアウト
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # ユーザー詳細
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("orders/", views.Order_create.as_view(), name="orders"),
    path("order_confirmation/", views.Order_confirmation.as_view(), name="order_confirmation"),
    path("succeed_order/", views.Succeed_order.as_view(), name="succeed_order"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("mypage/", views.Mypage.as_view(), name="mypage"), #マイページ
]