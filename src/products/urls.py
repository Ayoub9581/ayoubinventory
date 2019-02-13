#AYOUB AR
from django.conf.urls import url
from django.urls import path,include

from .views import (
		ProductListView,
		ProductDetailSlugView,
		ProductDownloadView,
		product_list_view
		)

app_name="products"
urlpatterns = [
	# path('', ProductListView.as_view(), name='list'),
	path('', product_list_view, name='list'),
	url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDownloadView.as_view(), name='download'),
]
