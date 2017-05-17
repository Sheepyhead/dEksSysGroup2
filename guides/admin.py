from django.contrib import admin
from .models import Guide, Category, Subcategory, GuideSuggestion
# Register your models here.

admin.site.register(Guide)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(GuideSuggestion)