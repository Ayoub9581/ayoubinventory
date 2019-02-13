from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
	"""
	User-related CRUD form
	"""
	class Meta:
		model = Address
		fields = [
			'nickname',
			'name',
			#'billing_profile',
			'address_type',
			'address_line_1',
			'address_line_2',
			'city',
			'country',
			'state',
			'postal_code'
		]

		widgets = {
			'nickname':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'name':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'country':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'city':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'postal_code':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'state':forms.Select(attrs={'class':'form-control unicase-form-control'}),
			'address_type':forms.Select(attrs={'class':'form-control unicase-form-control'}),
			'address_line_1':forms.TextInput(attrs={'class':'form-control unicase-form-control',}),
			'address_line_2':forms.TextInput(attrs={'class':'form-control unicase-form-control',}),
		}




class AddressCheckoutForm(forms.ModelForm):
	"""
	User-related checkout address create form
	"""
	class Meta:
		model = Address
		fields = [
			'nickname',
			'name',
			#'billing_profile',
			#'address_type',
			'address_line_1',
			'address_line_2',
			'city',
			'country',
			'state',
			'postal_code'
		]

		widgets = {
			'nickname':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'name':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'country':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'city':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'postal_code':forms.TextInput(attrs={'class':'form-control unicase-form-control text-input','placeholder':'','type':'text'}),
			'state':forms.Select(attrs={'class':'form-control unicase-form-control'}),
			'address_line_1':forms.TextInput(attrs={'class':'form-control unicase-form-control',}),
			'address_line_2':forms.TextInput(attrs={'class':'form-control unicase-form-control',}),

			}

			# #'billing_profile',
			# 'address_type':
			# 'address_line_1':
			# 'address_line_2':
			# 'city':
			# 'country':
			# 'state':
			# 'postal_code':
		# }
