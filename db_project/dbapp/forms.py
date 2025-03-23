from django import forms
from .models import Item

class ItemForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save(self, commit=True):
        item = Item(name=self.cleaned_data['name'], description=self.cleaned_data['description'])
        if commit:
            item.save()
        return item
