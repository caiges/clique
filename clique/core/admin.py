from django.contrib import admin
from models import *
from external_apps.categories.admin import BaseCategoryAdmin
from external_apps.pages.admin import BasePageAdmin
from external_apps.products.admin import BaseProductAdmin
from external_apps.recipes.admin import BaseRecipeAdmin

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('user',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(Article, ArticleAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ExerciseAdmin(admin.ModelAdmin):
    exclude = ('user',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(Exercise, ExerciseAdmin)

class ExerciseCategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(ExerciseCategory, ExerciseCategoryAdmin)

class FitnessTipAdmin(admin.ModelAdmin):
    exclude = ('user',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(FitnessTip, FitnessTipAdmin)

class FitnessTipCategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(FitnessTipCategory, FitnessTipCategoryAdmin)

class MythBusterAdmin(admin.ModelAdmin):
    exclude = ('user',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(MythBuster, MythBusterAdmin)

class MythBusterCategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(MythBusterCategory, MythBusterCategoryAdmin)

class NutritionTipAdmin(admin.ModelAdmin):
    exclude = ('user',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(NutritionTip, NutritionTipAdmin)

class NutritionTipCategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(NutritionTipCategory, NutritionTipCategoryAdmin)

class PageAdmin(BasePageAdmin):
    exclude = ('user',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(Page, PageAdmin)

class PageCategoryAdmin(BaseCategoryAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
admin.site.register(PageCategory, BaseCategoryAdmin)

class ProductAdmin(BaseProductAdmin):
    exclude = ('user',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/product.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/jquery.url.js', '/media/js/product-admin.js')
        
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(BaseCategoryAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(ProductCategory, ProductCategoryAdmin)

class RecipeAdmin(BaseRecipeAdmin):
    exclude = ('user',)
    
    class Media:
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/recipe-admin.js',)
    
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(Recipe, RecipeAdmin)

class RecipeCategoryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_description', 'category_image','default_category_page')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description','body')
        }),
    )
    
    class Media:
        css = {
            "all" : ('/media/css/admin/page.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/js/page-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
    
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
