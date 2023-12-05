from django.shortcuts import redirect
from django.views import generic

# def index(request):
#     return redirect("items:index")

#トップページ表示 
class HomeView(generic.TemplateView):
    template_name = "home.html"
