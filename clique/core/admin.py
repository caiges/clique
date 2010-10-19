from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Subcategory, SubcategoryAdmin)
