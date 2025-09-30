from django import forms


class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
    
    quantity = forms.TypedChoiceField(  
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Số lượng',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
