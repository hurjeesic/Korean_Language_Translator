from django import forms
from .models import Patter

class PatterForm(forms.ModelForm):

    class Meta:
        model = Patter
        fields = ('patter_str', 'meaning_short_str', 'meaning_long_str',)
