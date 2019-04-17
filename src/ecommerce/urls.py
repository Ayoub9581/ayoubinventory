
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView


from accounts.views import LoginView, RegisterView, GuestRegisterView
from addresses.views import (
	AddressCreateView,
	AddressListView,
	AddressUpdateView,
	checkout_address_create_view,
	checkout_address_reuse_view
	)
from analytics.views import SalesView, SalesAjaxView,go_dashboard,product_list_view_admin,customer_list_view,order_list_view
from billing.views import payment_method_view, payment_method_createview
from carts.views import cart_detail_api_view
from marketing.views import  MailChimpWebHookView,MarketingUpdateView
from orders.views import LibraryView

from products.views import add_product_upc

from .views import home_page, about_page, contact_page,app_page

urlpatterns = [
	path('', home_page, name='home'),
	path('bzoop/', app_page, name='app_page'),
	path('about/', about_page, name='about'),
	path('accounts/', RedirectView.as_view(url='/account')),
	path('account/', include("accounts.urls", namespace='account')),
	path('accounts/', include("accounts.passwords.urls")),
	path('address/', RedirectView.as_view(url='/addresses')),
	path('addresses/', AddressListView.as_view(), name='addresses'),
	path('addresses/create/', AddressCreateView.as_view(), name='address-create'),
	path('addresses/<pk>/', AddressUpdateView.as_view(), name='address-update'),
	path('analytics/sales/', SalesView.as_view(), name='sales-analytics'),
	path('analytics/sales/data/', SalesAjaxView.as_view(), name='sales-analytics-data'),
	path('analytics/dashboard/', go_dashboard, name='analytics-dashboard'),
	path('analytics/products/all/', product_list_view_admin, name='analytics-products'),
	path('analytics/customers/all/', customer_list_view, name='analytics-customers'),
	path('analytics/orders/all/', order_list_view, name='analytics-orders'),
	path('contact/', contact_page, name='contact'),
	path('login/', LoginView.as_view(), name='login'),
	path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
	path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
	path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('api/cart/', cart_detail_api_view, name='api-cart'),
	path('cart/', include("carts.urls", namespace='cart')),
	path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
	path('billing/payment-method/create/', payment_method_createview, name='billing-payment-method-endpoint'),
	path('register/', RegisterView.as_view(), name='register'),
	path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
	path('library/', LibraryView.as_view(), name='library'),
	path('orders/', include("orders.urls", namespace='orders')),
	path('products/', include("products.urls", namespace='products')),
	path('add/product/', add_product_upc, name="add-product-upc"),
	path('category/', include("categories.urls", namespace='subcategory')),
	path('search/', include("search.urls", namespace='search')),
	path('settings/', RedirectView.as_view(url='/account')),
	path('settings/email/', MarketingUpdateView.as_view(), name='marketing-pref'),
	path('webhooks/mailchimp/', MailChimpWebHookView.as_view(), name='webhooks-mailchimp'),
	path('admin/', admin.site.urls),
]


if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
