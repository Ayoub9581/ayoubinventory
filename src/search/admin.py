from django.contrib import admin
from .models import Search




class SearchAdmin(admin.ModelAdmin):
    list_display = ['query','timestamp']




admin.site.register(Search, SearchAdmin)
