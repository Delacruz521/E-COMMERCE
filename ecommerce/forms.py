from django import forms
from .models import *

class admin_items_forms(forms.ModelForm):
    class Meta:
        model = admin_items
        fields = ['name_items', 'price_items']

class account(forms.ModelForm):
    class Meta:
        model = user_create
        fields = ['id_user', 'username', 'email', 'password', 'number']
