#AYOUB AR
from django.shortcuts import render
from .models import Category,SubCategory
from products.models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from analytics.mixins import ObjectViewedMixin
from django.http import Http404
from ecommerce.utils import unique_slug_generator






def sub_category_detail(request,slug):
	instance = get_object_or_404(SubCategory,slug=slug)
	if instance.slug is None:
		instance.slug = unique_slug_generator(instance.slug)
	context = {
		'instance':instance,
	}
	return render(request,'categories/detail.html',context)
