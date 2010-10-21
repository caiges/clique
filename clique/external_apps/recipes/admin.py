from django.contrib import admin
from models import *

class RecipeAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/product-admin.js',)
    
admin.site.register(Recipe, RecipeAdmin)