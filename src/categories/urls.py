from django.urls import path,include
from django.conf.urls import url
from .views import sub_category_detail


app_name = 'subcategory'
urlpatterns = [
	   path('<slug:slug>/',sub_category_detail, name='detail'),

]
