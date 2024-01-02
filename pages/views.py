from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .models import Contact
from .forms import ContactForm


class Tosacha(generic.TemplateView):
    template_name = "pages/tosatea.html"

class Privacy_policy(generic.TemplateView):
    template_name = "pages/privacy_policy.html"
    
class Contact_form(FormView):
    template_name = "pages/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact_complete')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class Contact_complete(TemplateView):
    template_name = "pages/contact_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context
        
class Contact_list(LoginRequiredMixin, generic.ListView):
    model = Contact
    template_name = "pages/contact_list.html"
    ordering = "-create_date"
    
    def get_queryset(self):
        return Contact.objects.all()
    
    def get_context_data(self, **kwargs):
        contact = Contact.objects.all()
        context = super().get_context_data(**kwargs)
        context["title"] = "お問合せ管理"
        return context
    
class Contact_detail(LoginRequiredMixin, generic.DetailView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("pages:contact_list")
    template_name = "pages/contact_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お問合せ詳細"
        return context