from elibrary_app.models import Catalogue
from django import forms

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = "__all__"

        widgets = {
            'title':forms.widgets.TextInput(attrs={
                'class':'form-control'
            }),
            'ISBN':forms.widgets.TextInput(attrs={
                'class':'form-control'
            }),
            'author':forms.widgets.TextInput(attrs={
                'class':'form-control'
            }),
            'price':forms.widgets.NumberInput(attrs={
                'class':'form-control'
            }),
            'availability':forms.widgets.Select(attrs={
                'class':'form-control'
            })
        }