from django import forms
from .models import Item

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name", 
            "description", 
            "category",
            "price",
            "stock",
            "image"
        ]
 
class CartUpdateForm(forms.Form):

    amount = forms.IntegerField(
        label="注文数",
        required=True,
        widget=forms.NumberInput() 
    )
