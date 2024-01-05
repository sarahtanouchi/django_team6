from django.urls import path
from . import views
from .views import ContactView, ContactComplete, ContactUpdate
 
app_name = "pages"
 
urlpatterns = [
    path("tosacha/", views.Tosacha.as_view(), name="tosacha"),
    path("privacy_policy/", views.Privacy_policy.as_view(), name="privacy_policy"), 
    path("contact/", views.ContactView.as_view(), name="contact"), 
    # path("contact_review/", ContactReview.as_view(), name="contact_review"),
    path("contact_complete/", views.ContactComplete.as_view(), name="contact_complete"),
    path("contact_list/", views.ContactList.as_view(), name="contact_list"),
    path("contact_update/<int:pk>/", views.ContactUpdate.as_view(), name="contact_update"),
]