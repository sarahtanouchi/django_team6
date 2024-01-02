from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class Tosacha(generic.TemplateView):
    template_name = "pages/tosatea.html"

class Privacy_policy(generic.TemplateView):
    template_name = "pages/privacy_policy.html"
    
class ContactForm(FormView):
    template_name = "pages/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResult(TemplateView):
    template_name = "pages/contact_result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context
    
