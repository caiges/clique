import uuid

from django.db import models
from external_apps.categories.models import BaseCategory
from external_apps.contentassociation.models import BaseContentAssociation
from external_apps.pages.models import BasePage
from external_apps.products.models import BaseProduct
from external_apps.recipes.models import BaseRecipe

class ContentAssociation(BaseContentAssociation):
    target_model_field = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link = models.CharField(max_length = 1000, blank = True, null = True, default = None)
    target_model_link_name = models.CharField(max_length = 36, blank = False, null = False, default = uuid.uuid4())

class Page(BasePage):
    category = models.ManyToManyField('PageCategory', related_name = 'page_categories', blank = False, null = False)

    @models.permalink
    def get_absolute_url(self):
        return ('page_show', [str(self.id)])

class PageCategory(BaseCategory):
    
    class Meta(BaseCategory.Meta):
        verbose_name_plural = 'Page Categories'
    
class Product(BaseProduct):
    category = models.ManyToManyField('ProductCategory', related_name = 'product_categories', blank = False, null = False)
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d')
    store_link = models.CharField(max_length = 255, blank = True, null = True, default = None)

    @models.permalink
    def get_absolute_url(self):
        return ('product_show', [str(self.id)])
        
    def get_associated_content_items(self):
        content_associations = ContentAssociation.objects.filter(source_model__exact = self.__class__.__name__.lower(), source_model_id = self.id)
        #content_association_target_instances = [getattr(__file__, ca.target_model.capitalize()).objects.get(pk = ca.target_model_id) for ca in content_associations]
        print content_associations
        #return content_association_target_instances

class ProductCategory(BaseCategory):
    
    class Meta(BaseCategory.Meta):
        verbose_name_plural = 'Product Categories'

class Recipe(BaseRecipe):
    category = models.ManyToManyField('RecipeCategory', related_name = 'recipe_categories', blank = False, null = False)
    
    @models.permalink
    def get_absolute_url(self):
        return ('recipe_show', [str(self.id)])
    
class RecipeCategory(BaseCategory):
    
    class Meta(BaseCategory.Meta):
        verbose_name_plural = 'Recipe Categories'
