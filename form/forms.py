from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


class ValueFileForm(forms.Form):
    title = forms.CharField(max_length=50)