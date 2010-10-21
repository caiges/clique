from django.contrib import admin
from models import *
from external_apps.products.admin import BaseProductAdmin

class CategoryAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(BaseProductAdmin):
    class Media:
        css = {
            "all" : ('/media/css/admin/product.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/product-admin.js',)

admin.site.register(Product, ProductAdmin)