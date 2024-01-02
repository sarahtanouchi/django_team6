from django.urls import path
from . import views
 
app_name = "pages"
 
urlpatterns = [
    path("tosacha/", views.Tosacha.as_view(), name="tosacha"),
    path("privacy_policy/", views.Privacy_policy.as_view(), name="privacy_policy"), 
    path("contact/", views.ContactForm.as_view(), name="contact_form"), 
    path('contact_result/', views.ContactResult.as_view(), name='contact_result'),
]