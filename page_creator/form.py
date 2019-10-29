from django import forms
from .models import PageCreator


class PageCreatorForm(forms.ModelForm):

    class Meta:
        model = PageCreator
        fields = ('title', )
