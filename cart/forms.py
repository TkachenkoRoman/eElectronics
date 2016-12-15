from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_ONE_QUANTITY_CHOICES =[(i, str(i)) for i in range(1, 2)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartAddOneProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_ONE_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)