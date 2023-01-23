from django import forms
 
class CartUpdateForm(forms.Form):

    amount = forms.IntegerField(
        label="注文数",
        required=True,
        widget=forms.NumberInput() 
    )
