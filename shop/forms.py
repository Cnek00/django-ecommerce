from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, f"{i} ⭐") for i in range(1, 6)],
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Puanınız"
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        label="Yorumunuz"
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']


from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Adet")
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput())
