from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import  UpdateView, View
from django.contrib.messages.views import SuccessMessageMixin
from .forms import MarketingForm
from .models import Marketing
from .utils import MailChimp
from .mixins import CsrfExemptMixin

MAILCHIMP_EMAIL_LIST_ID     =  getattr(settings,'MAILCHIMP_EMAIL_LIST_ID', None)

class MarketingUpdateView(SuccessMessageMixin,UpdateView):
	form_class = MarketingForm
	template_name = 'base/forms.html' # create this
	success_url = '/settings/email/'
	success_message = 'Your email Prefernces have been updated. thank you'

	def dispatch(self, *args, **kwargs):
		user = self.request.user
		if not user.is_authenticated:
			return redirect('/accounts/login/?next=/settings/email/')
		return super(MarketingUpdateView, self).dispatch(*args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(MarketingUpdateView,self).get_context_data(*args,**kwargs)
		context['title'] = 'Marketing Preferences'
		return context

	def get_object(self):
		user = self.request.user
		obj,created = Marketing.objects.get_or_create(user=user) #get_absolute_url
		return obj



"""
data[ip_opt]: 41.142.205.39
data[web_id]: 11168371
type: unsubscribe
data[reason]: manual
data[merges][EMAIL]: ayoubarahmat9@gmail.com
fired_at: 2019-01-31 02:08:44
data[email]: ayoubarahmat9@gmail.com
data[merges][ADDRESS]:
data[list_id]: 3884f8f9b9
data[id]: 746703f068
data[merges][PHONE]:
data[merges][LNAME]:
data[merges][FNAME]:
data[action]: unsub
data[email_type]: html
"""

class MailChimpWebHookView(CsrfExemptMixin,View):
	def post(self,request, *args, **kwargs):
		data = request.POST
		list_id = data.get('data[list_id]')
		if str(list_id) == str(MAILCHIMP_EMAIL_LIST_ID):
			hook_type = data.get('type')
			email = data.get('data[email]')
			response_status, response = MailChimp().check_subscription_status(email)
			sub_status =response['status']
			is_subbed = None
			mailchimp_subbed = None
			if sub_status == "subscribed":
				is_subbed,mailchimp_subbed = (True,True)
			elif sub_status == "unsubscribed":
				is_subbed,mailchimp_subbed = (False,False)

			if is_subbed is not None and mailchimp_subbed is not None:
				qs = Marketing.objects.filter(use__email__iexact=email)
				if qs.exists():
					qs.update(
							subscribed=is_subbed,
							mailchimp_subscribed=mailchimp_subbed
							,mailchimp_msg=str(data)
							)
		return HttpResponse("thank you", status=200)


#
# def mailchimp_webhook_view(request):
# 	data = request.POST
# 	list_id = data.get('data[list_id]')
# 	if str(list_id) = str(MAILCHIMP_EMAIL_LIST_ID):
# 		hook_type = data.get('type')
# 		email = data.get('data[email]')
# 		response_status, response = MailChimp().check_subscription_status(email)
# 		sub_status =response['status']
# 		is_subbed = None
# 		mailchimp_subbed = None
# 		if sub_status == "subscribed":
# 			is_subbed,mailchimp_subbed = (True,True)
# 		elif sub_status == "unsubscribed":
# 			is_subbed,mailchimp_subbed = (False,False)
#
# 		if is_subbed is not None and mailchimp_subbed is not None:
# 			qs = Marketing.objects.filter(use__email__iexact=email)
# 			if qs.exists():
# 				qs.update(
# 						subscribed=is_subbed,
# 						mailchimp_subscribed=mailchimp_subbed
# 						,mailchimp_msg=str(data)
# 						)
# 	return HttpResponse("thank you", status=200)
