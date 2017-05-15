from django import forms


class SubmitNewGuide(forms.Form):
    Title = forms.CharField()
    Text = forms.CharField(widget=forms.Textarea)
