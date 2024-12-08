from django import forms
from smartshelfapp.models import Shelf

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ['number', 'location', 'date', 'due_date', 'weight', 'price']
