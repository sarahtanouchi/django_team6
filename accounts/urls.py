from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

 
app_name = "accounts"
 
urlpatterns = [
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),
    path("login/", views.Login.as_view(), name="login"), # ログイン
    path("logout/", views.Logout.as_view(), name="logout"), # ログアウト
    path("complete/", views.Complete.as_view(), name="complete"), # 完了ページ
    # path("resetting/", views.Resetting.as_view(), name="resetting"), #パスワード再設定手続き
    # path("reset/", views.Reset.as_view(), name="reset"), #パスワード再設定
    # path("recomplete/", views.Recomplete.as_view(), name="recomplete"), # パスワード再設定完了
    # path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # ユーザー詳細
    # path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
    path("orders/", views.Order_create.as_view(), name="orders"),
    path("order_confirmation/", views.Order_confirmation.as_view(), name="order_confirmation"),
    path("succeed_order/", views.Succeed_order.as_view(), name="succeed_order"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("mypage/", views.Mypage.as_view(), name="mypage"), #マイページ
    # path("favorite/", views.Favorite.as_view(), name="favorite"), # お気に入り
    path("order_history/", views.Order_history.as_view(), name="order_history"), #注文履歴
]