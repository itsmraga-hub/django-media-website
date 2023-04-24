from django import forms


class AddImageForm(forms.Form):
    image = forms.ImageField()
    name = forms.CharField(max_length=255)