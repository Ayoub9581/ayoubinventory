#AYOUB AR
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from .models import Search
from analytics.utils import get_client_ip

class SearchProductView(ListView):
	template_name = "search/view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get('q')
		context['query'] = query
		print(query)
		Search.objects.create(query=query,ip_address=get_client_ip(self.request))
		return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		method_dict = request.GET
		query = method_dict.get('q', None) # method_dict['q']
		if query is not None:
			return Product.objects.search(query)
		return Product.objects.featured()
		'''
		__icontains = field contains this
		__iexact = fields is exactly this
		'''
