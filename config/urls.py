from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("items/", include("items.urls")),
    # path("", views.index),  #仮削除　12/5 
    path("", views.HomeView.as_view(), name="home"), #トップページ表示追加
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
