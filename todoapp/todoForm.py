from .models import tasks
from django import forms
class todoFrom(forms.ModelForm):
    class Meta:
        model= tasks
        fields = ['name','priority','date']
