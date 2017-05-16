from django import forms
from .models import Category

class SubmitNewGuide(forms.Form):
    title = forms.CharField()    
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    short_description = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

class SubmitNewRequest(forms.Form):
	name = forms.CharField()
	category = forms.ModelChoiceField(queryset=Category.objects.all())
	description = forms.CharField()
