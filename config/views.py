from django.views import generic
from items.models import Information, Item

#トップページ表示 
class HomeView(generic.TemplateView):
    template_name = "pages/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["information_list"] = Information.objects.all()
        context["recommended_items"] = Item.objects.filter(recommended=True)
        return context
