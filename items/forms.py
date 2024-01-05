from django import forms
from .models import Item, Area, Item_type, Occasion, Tea_set_type, Tea_type, Taste, Flavor, Image, Review, Favorite, Information, Coupon



class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name", 
            "price",
            "status",
            "recommended",
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
            # "image",
            # "second_image",
            "item_images",
        ]
        widgets = {
            "description":forms.Textarea(attrs={"rows":4}),
            'item_images':forms.CheckboxSelectMultiple()
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
        
class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            "name",
            "image"
        ]
        
class CartUpdateForm(forms.Form):

    amount = forms.IntegerField(
        label="注文数",
        required=True,
        widget=forms.NumberInput() 
    )

class InformationCreateForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = [
            "title",
            "body",
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "rate",
            "comment"
        ]
        widgets = {
            "rate": forms.RadioSelect(choices=Review.CHOICES),
        }
    def __init__(self, *args, **kwargs):
        item = kwargs.pop('item', None)
        super().__init__(*args, **kwargs)
  
class FavoriteAddForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            "item",
        ]
        
class SearchForm(forms.Form):
    search_term = forms.CharField(
        label='', 
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '商品名で検索'
            
        })
    )
    
class CouponCreateForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = [
            "code",
            "discount_percent",
            "description",
            "deleted",
        ]
        widgets = {
            "description":forms.Textarea(attrs={"rows":4}),
        }
    