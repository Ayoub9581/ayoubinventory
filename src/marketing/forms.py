#AYOUB AR
from django import forms
from .models import Marketing


class MarketingForm(forms.ModelForm):
	# subscribed = forms.BooleanField(label='Receive  Marketing Email ?', required=False)
	class Meta:
		model     = Marketing
		fields    = ['subscribed',]
		widgets = {
			'subscribed':forms.CheckboxInput(attrs={'class':'mdl-checkbox__input','type':"checkbox",'id':"checkbox-1"}),
		}
