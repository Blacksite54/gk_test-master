from django import forms
from menus.models import MenuItem


class MenuItemFormSerializer(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = (
            'name',
            'parent',
            'named_url_parts',
            'url',
        )

    def clean_explicit_url(self):
        return self.cleaned_data['named_url_parts'] or None

    def clean_named_url(self):
        return self.cleaned_data['url'] or None
