from django import forms


class AddImageForm(forms.Form):
    image = forms.ImageField()
    name = forms.CharField(max_length=255)


class AddVideoForm(forms.Form):
    file = forms.FileField()
    title = forms.CharField(max_length=255)


class AddAudioForm(forms.Form):
    file = forms.FileField()
    title = forms.CharField(max_length=255)

