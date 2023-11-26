from django import forms
from .models import Item, Area

class AreaCreateForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = [
            "name",
            "description"
        ]

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name", 
            "price",
            "status",
            "stock",
            "description",
            "item_type",
            "occasion",
            "tea_type",
            "taste",
            "area",
            "image",
            "second_image",
            
        ]
 
class CartUpdateForm(forms.Form):

    amount = forms.IntegerField(
        label="注文数",
        required=True,
        widget=forms.NumberInput() 
    )
