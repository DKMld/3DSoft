from django import forms


class ProductSearchForm(forms.Form):

    search_input = forms.CharField(
        max_lenght=100,
        required=False,

    )