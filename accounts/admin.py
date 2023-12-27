from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Destination, Order, Order_detail

User = get_user_model()
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Destination)
admin.site.register(Order_detail)
