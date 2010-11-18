import os

from django.contrib import admin

from models import *
from external_apps.categories.admin import BaseCategoryAdmin
from external_apps.pages.admin import BasePageAdmin
from external_apps.products.admin import BaseProductAdmin
from external_apps.recipes.admin import BaseRecipeAdmin

class ArticleAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'body', 'categories', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
        
admin.site.register(Article, ArticleAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ExerciseAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'body', 'exercise_image', 'remove_exercise_image', 'categories', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_exercise_image and inst.exercise_image != '':
            if os.path.exists(inst.exercise_image.path):
                os.remove(inst.exercise_image.path)
            inst.exercise_image = ''
            inst.remove_exercise_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
        
admin.site.register(Exercise, ExerciseAdmin)

class ExerciseCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(ExerciseCategory, ExerciseCategoryAdmin)

class FitnessTipAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'body', 'categories', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
        
admin.site.register(FitnessTip, FitnessTipAdmin)

class FitnessTipCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(FitnessTipCategory, FitnessTipCategoryAdmin)

class FunctionalAttributeAdmin(admin.ModelAdmin):
    pass

admin.site.register(FunctionalAttribute, FunctionalAttributeAdmin)

class MythBusterAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'body', 'categories', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(MythBuster, MythBusterAdmin)

class MythBusterCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(MythBusterCategory, MythBusterCategoryAdmin)

class NutritionalAttributeAdmin(admin.ModelAdmin):
    pass

admin.site.register(NutritionalAttribute, NutritionalAttributeAdmin)

class NutritionTipAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'body', 'categories', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
        
admin.site.register(NutritionTip, NutritionTipAdmin)

class NutritionTipCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(NutritionTipCategory, NutritionTipCategoryAdmin)

class PageAdmin(BasePageAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'body', 'categories', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'include_on_primary_navigation', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(Page, PageAdmin)

class PageCategoryAdmin(BaseCategoryAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)
    
    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(PageCategory, PageCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'external_url', 'meta_description', 'meta_keywords', 'long_description', 'product_details', 'mobile_description', 'product_image', 'remove_product_image', 'supplement_information_image', 'remove_supplement_information_image', 'store_link', 'categories', 'functional_attributes', 'nutritional_attributes', 'for_athletes', 'make_live', 'featured', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'product_categories', 'language', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name', 'language',)
    save_on_top = True
    search_fields = ('name', 'categories__name',)
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)
        
    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_product_image and inst.product_image != '':
            if os.path.exists(inst.product_image.path):
                os.remove(inst.product_image.path)
            inst.product_image = ''
            inst.remove_product_image = False
        if inst.remove_supplement_information_image and inst.supplement_information_image != '':
            if os.path.exists(inst.supplement_information_image.path):
                os.remove(inst.supplement_information_image.path)
            inst.supplement_information_image = ''
            inst.remove_supplement_information_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(BaseCategoryAdmin):
    exclude = ('user',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'make_live', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(ProductCategory, ProductCategoryAdmin)

class RecipeAdmin(BaseRecipeAdmin):
    actions = None
    exclude = ('user',)
    fieldsets = (('Basic Info', {
                                 'fields' : ('name', 'page_title', 'url', 'meta_description', 'meta_keywords', 'ingredients', 'directions', 'categories', 'also_enjoy', 'make_live', 'featured', 'include_on_primary_navigation', 'sort_order', 'language')
                                 }
    ),)
    list_display = ('name', 'make_live', 'sort_order')
    list_editable = ('make_live', 'sort_order',)
    ordering = ('sort_order', 'name',)
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)
    
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit = False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance
        
admin.site.register(Recipe, RecipeAdmin)

class RecipeCategoryAdmin(admin.ModelAdmin):
    exclude = ('user', 'category_description', 'default_category',)
    fieldsets = (('Category Info', {
            'fields': ('name', 'category_image', 'remove_category_image', 'language')
        }),
        ('Page Info', {
            'fields': ('page_title', 'url', 'meta_description', 'meta_keywords', 'body')
        }),
    )
    save_on_top = True
    
    class Media:
        css = {
            "all" : ('/media/css/admin/common.css',)
        }
        js = ('/media/js/jquery-1.4.2.js', '/media/js/jquery.url.js', '/media/js/tiny_mce/tiny_mce_jquery_src.js', '/media/filebrowser/js/TinyMCEAdmin.js', '/media/js/tinymce_addons.js', '/media/js/common-admin.js',)

    def save_model(self, request, obj, form, change): 
        inst = form.save(commit = False)
        if inst.remove_category_image and inst.category_image != '':
            if os.path.exists(inst.category_image.path):
                os.remove(inst.category_image.path)
            inst.category_image = ''
            inst.remove_category_image = False
        inst.user = request.user
        inst.save()
        form.save_m2m()
        return inst
    
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
