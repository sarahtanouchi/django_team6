from django.urls import path
from . import views
from .views import Contact_form, Contact_complete, Contact_detail
 
app_name = "pages"
 
urlpatterns = [
    path("tosacha/", views.Tosacha.as_view(), name="tosacha"),
    path("privacy_policy/", views.Privacy_policy.as_view(), name="privacy_policy"), 
    path("contact/", views.Contact_form.as_view(), name="contact_form"), 
    path("contact_complete/", views.Contact_complete.as_view(), name="contact_complete"),
    path("contact_list/", views.Contact_list.as_view(), name="contact_list"),
    path("contact_detail/<int:pk>/", views.Contact_detail.as_view(), name="contact_detail"),
]