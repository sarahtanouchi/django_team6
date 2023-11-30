from django import forms
from .models import Item, Area, Item_type, Occasion, Tea_set_type, Tea_type, Taste, Flavor



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
            "tea_set_type",
            "tea_type",
            "taste",
            "second_taste",
            "flavor",
            "area",
            "image",
            "second_image",
        ]
        widgets = {
            "description":forms.Textarea(attrs={"rows":4})
        }
        
class ItemTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Item_type
        fields = [
            "name"
        ]
 
class OccasionCreateForm(forms.ModelForm):
    class Meta:
        model = Occasion
        fields = [
            "name"
        ]

class TeaSetTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Tea_set_type
        fields = [
            "name"
        ]

class TeaTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Tea_type
        fields = [
            "name"
        ]
        
class TasteCreateForm(forms.ModelForm):
    class Meta:
        model = Taste
        fields = [
            "name"
        ]

class FlavorCreateForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = [
            "name"
        ]


class AreaCreateForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = [
            "name",
            "description"
        ]
        
class CartUpdateForm(forms.Form):

    amount = forms.IntegerField(
        label="注文数",
        required=True,
        widget=forms.NumberInput() 
    )
