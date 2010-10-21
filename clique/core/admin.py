from django.contrib import admin
from models import *
from external_apps.categories.admin import BaseCategoryAdmin
from external_apps.pages.admin import BasePageAdmin
from external_apps.products.admin import BaseProductAdmin
from external_apps.recipes.admin import BaseRecipeAdmin

class PageAdmin(BasePageAdmin):
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

admin.site.register(Page, PageAdmin)

class PageCategoryAdmin(BaseCategoryAdmin):
    pass
    
admin.site.register(PageCategory, BaseCategoryAdmin)

class ProductAdmin(BaseProductAdmin):
    
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/product.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/product-admin.js',)

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(BaseCategoryAdmin):
    pass
    
admin.site.register(ProductCategory, ProductCategoryAdmin)

class RecipeAdmin(BaseRecipeAdmin):
    class Media:
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/product-admin.js',)

admin.site.register(Recipe, RecipeAdmin)
