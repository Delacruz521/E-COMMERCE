from django import forms
from .models import *

class admin_items_forms(forms.ModelForm):
    class Meta:
        model = admin_items
        fields = ['name_items', 'price_items']