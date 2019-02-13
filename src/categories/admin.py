#AYOUB AR
from django.contrib import admin


from .models import Category,SubCategory


class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('id','title','slug','timestamp')
	list_editable = ['slug']

admin.site.register(Category)
admin.site.register(SubCategory,SubCategoryAdmin)
