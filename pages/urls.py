from django.urls import path
from . import views
 
app_name = "pages"
 
urlpatterns = [
    path("privacy_policy/", views.PrivacyPolicy.as_view(), name="privacy_policy"), #プライバシーポリシー
]