#AYOUB AR
from django.db import models
from django.urls import reverse
from billing.models import BillingProfile

ADDRESS_TYPES = (
	('billing', 'Billing address'),
	('shipping', 'Shipping address'),
)

STATE_TYPES = (
	('AL-Alabama','Alabama'),
	('AZ-Arizona','Arizona'),
	('AR-Arkansas','Arkansas'),
	('CA-California','California'),
	('CO-Colorado','Colorado'),
	('CT-Connecticut','Connecticut'),
	('DE-Delaware','Delaware'),
	('DC-District of Columbia','District of Columbia'),
	('FL-Florida','Florida'),
	('GA-Georgia','Georgia'),
	('ID-Idaho','Georgia'),
	('IL-Illinois','Illinois'),
	('IN-Indiana','Indiana'),
	('IA-Iowa','Iowa'),
	('KS-Kansas','Kansas'),
	('KY-Kentucky','Kentucky'),
	('LA-Louisiana','Louisiana'),
	('ME-Maine','Maine'),
	('MD-Maryland','Maryland'),
	('MA-Massachusetts','Massachusetts'),
	('MN-Minnesota','Minnesota'),
	('MI-Michigan','Michigan'),
	('MS-Mississippi','Mississippi'),
	('MO-Missouri','Missouri'),
	('MT-Montana','Montana'),
	('NE-Nebraska','Nebraska'),
	('NV-Nevada','Nevada'),
	('NH-New Hampshire','New Hampshire'),
	('NJ-New Jersey','New Jersey'),
	('NM-New Mexico','New Mexico'),
	('NY-New York','New York'),
	('NC-North Carolina','North Carolina'),
	('ND-North Dakota','North Dakota'),
	('OH-Ohio','Ohio'),
	('OK-Oklahoma','Oklahoma'),
	('OR-Oregon','Oregon'),
	('PA-Pennsylvania','Pennsylvania'),
	('RI-Rhode Island','Rhode Island'),
	('SC-South Carolina','South Carolina'),
	('SD-South Dakota','South Dakota'),
	('TN-Tennessee','Tennessee'),
	('TX-Texas','Texas'),
	('UT-Utah','Utah'),
	('VT-Vermont','Vermont'),
	('VA-Virginia','Virginia'),
	('WA-Washington','Washington'),
	('WV-West Virginia','West Virgini'),
	('WI-Wisconsin','Wisconsin'),
	('WY-Wyoming','Wyoming'),
)




class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
	name            = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
	nickname        = models.CharField(max_length=120, null=True, blank=True, help_text='Internal Reference Nickname')
	address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
	address_line_1  = models.CharField(max_length=120)
	address_line_2  = models.CharField(max_length=120, null=True, blank=True)
	city            = models.CharField(max_length=120)
	country         = models.CharField(max_length=120, default='United States of America')
	state           = models.CharField(max_length=120,choices=STATE_TYPES)
	postal_code     = models.CharField(max_length=120)

	def __str__(self):
		if self.nickname:
			return str(self.nickname)
		return str(self.address_line_1)

	def get_absolute_url(self):
		return reverse("address-update", kwargs={"pk": self.pk})

	def get_short_address(self):
		for_name = self.name
		if self.nickname:
			for_name = "{} | {},".format( self.nickname, for_name)
		return "{for_name} {line1}, {city}".format(
				for_name = for_name or "",
				line1 = self.address_line_1,
				city = self.city
			)

	def get_address(self):
		return "{for_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
				for_name = self.name or "",
				line1 = self.address_line_1,
				line2 = self.address_line_2 or "",
				city = self.city,
				state = self.state,
				postal= self.postal_code,
				country = self.country
			)
