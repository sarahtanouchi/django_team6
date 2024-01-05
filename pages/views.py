from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseNotAllowed
from .models import Contact
from .forms import ContactForm, ContactManagementForm



class Tosacha(generic.TemplateView):
    template_name = "pages/tosatea.html"

class Privacy_policy(generic.TemplateView):
    template_name = "pages/privacy_policy.html"

    
class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact_complete')

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)

# class ContactReview(FormView):
#     template_name = "pages/contact_review.html"
#     form_class = ContactForm
#     success_url = reverse_lazy('pages:contact_complete')

#     def form_valid(self, form):
#         # フォームの内容をセッションに保存しておく
#         self.request.session['contact_form_data'] = form.cleaned_data
#         return super().form_valid(form)

class ContactComplete(TemplateView):
    template_name = "pages/contact_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせを送信しました。"
        return context
        
class ContactList(LoginRequiredMixin, generic.ListView):
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
    
class ContactUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Contact
    form_class = ContactManagementForm
    template_name = "pages/contact_update.html"
    success_url = reverse_lazy("pages:contact_list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "お問合せ詳細"
        return context
        
        
# 確認画面あり問合せフォーム(完了画面エラー)
# class ContactView(FormView):
#     template_name = "pages/contact.html"
#     form_class = ContactForm
#     success_url = reverse_lazy('pages:contact_review')

#     def form_valid(self, form):
#         # フォームの内容をセッションに保存しておく
#         self.request.session['contact_data'] = form.cleaned_data
#         return super().form_valid(form)

# class ContactReview(FormView):
#     template_name = "pages/contact_review.html"
#     form_class = ContactForm
#     success_url = reverse_lazy('pages:contact_complete')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form_data'] = self.request.session.get('contact_data', {})
#         return context

#     def form_valid(self, form):
#         # フォームの内容をセッションに保存しておく
#         self.request.session['contact_data'] = form.cleaned_data
#         contact_data = form.cleaned_data
#         form.save()
#         form.send_email()
        
#         return super().form_valid(form)

# class ContactComplete(TemplateView):
#     template_name = "pages/contact_complete.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['success'] = "お問い合わせを送信しました。"
        
#         return context