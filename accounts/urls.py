from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

 
app_name = "accounts"
 
urlpatterns = [
    path("input/", views.Input.as_view(), name="input"), #input
    path("sign_up/", views.SignUp.as_view(), name="sign_up"),  # 確定
    path("login/", views.Login.as_view(), name="login"), # ログイン
    path("logout/", views.Logout.as_view(), name="logout"), # ログアウト
    path("complete/", views.Complete.as_view(), name="complete"), # 完了ページ
    path("resetting/", views.Resetting.as_view(), name="resetting"), #パスワード再設定手続き
    path("reset/", views.Reset.as_view(), name="reset"), #パスワード再設定
    path("recomplete/", views.Recomplete.as_view(), name="recomplete"), # パスワード再設定完了
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # ユーザー詳細
    path("update/<int:pk>/", views.Update.as_view(), name="update"), # 編集
]
