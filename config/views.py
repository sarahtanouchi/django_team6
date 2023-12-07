from django.views import generic

#トップページ表示 
class HomeView(generic.TemplateView):
    template_name = "pages/home.html"
