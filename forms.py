from django import forms
from .models import mycurd


class myCurdForm(forms.ModelForm):
    class Meta:
        model = mycurd
        fields = ['name', 'due_date']

