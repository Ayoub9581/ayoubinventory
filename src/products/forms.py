from django import forms
from .models import Product
from django.contrib import  messages

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('upc',)

	widgets = {
		'upc':forms.TextInput(attrs={'class':'form-control','type':'text','required':''}),

	}

	def clean_upc(self):
		upc = self.cleaned_data['upc']
		if len(str(upc)) != 12:
			raise forms.ValidationError(' length must be 12')
		elif str(upc).startswith("2") or str(upc).startswith("4"):
			raise forms.ValidationError('UPCs that start with "2" or "4" are meant for internal use. Try Expanded mode')

		return upc






# NB : make a better algorithm Today 23/02/2019
