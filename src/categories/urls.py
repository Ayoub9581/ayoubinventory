from django.urls import path,include
from django.conf.urls import url
from .views import sub_category_detail, category_datails


app_name = 'subcategory'
urlpatterns = [
	   path('<int:id>/',category_datails, name='category-detail'),
	   path('<slug:slug>/',sub_category_detail, name='detail'),

]
