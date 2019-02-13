#AYOUB AR
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from ecommerce.utils import unique_slug_generator

class CategoryQuerSet(models.query.QuerySet):
	def draft(self):
		return self.filter(draft=True)


class CategoryManager(models.Manager):
	def get_queryset(self):
		return CategoryQuerSet(self.model, using=self._db)

	def draft(self):
		return self.get_queryset().draft()

class Category(models.Model):
	category_name = models.CharField(unique=True,max_length=120, null=True, blank=True)
	icon = models.ImageField(upload_to='category/icon', null=True,blank=True)
	fontawesome = models.CharField(max_length=30, null=True, blank=True)
	draft = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category_name

	def get_absolute_url(self):
		pass

	@property
	def get_products(self):
		return Product.objects.filter()

	objects = CategoryManager()


class SubCategory(models.Model):
	title   = models.CharField(unique=True,max_length=120)
	slug = models.SlugField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("subcategory:detail", kwargs={"slug": self.slug})

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=SubCategory)
