from django import forms
from .models import Category, Subcategory

class SubmitNewGuide(forms.Form):
	title = forms.CharField()    
	category = forms.ModelChoiceField(queryset=Category.objects.all())  
	subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all())  
	short_description = forms.CharField()
	text = forms.CharField(widget=forms.Textarea)

class SubmitNewRequest(forms.Form):
	name = forms.CharField()
	category = forms.ModelChoiceField(queryset=Category.objects.all())
	description = forms.CharField()

class SubmistChangeRequest(forms.Form):
	description = forms.CharField()
