#AYOUB AR
from django.contrib import admin
from .models import Marketing

class MarketingAdmin(admin.ModelAdmin):
	list_display = ('__str__','subscribed', 'updated')
	readonly_fields = ['mailchimp_subscribed','timestamp','updated']
	class Meta:
		model  = Marketing
		fields = [
				'user',
				'subscribed',
				'mailchimp_msg',
				'mailchimp_subscribed',
				'timestamp',
				'updated'
		]


admin.site.register(Marketing,MarketingAdmin)
