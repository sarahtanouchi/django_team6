from django.shortcuts import render
from django.views import generic

#トップページ表示 
class PrivacyPolicy(generic.TemplateView):
    template_name = "pages/privacy_policy.html"