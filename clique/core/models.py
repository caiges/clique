from django.db import models
from external_apps.categories.models import BaseCategory
from external_apps.pages.models import BasePage
from external_apps.products.models import BaseProduct
from external_apps.recipes.models import BaseRecipe

class ContentAssocation(models.Model):
    model_name = models.CharField(max_length = 100, blank = False, null = False)
    model_id = models.IntegerField(blank = False, null = False)
    target_model_name = models.CharField(max_length = 100, blank = False, null = False)
    target_model_id = models.IntegerField(blank = False, null = False)

class Page(BasePage):
    category = models.ForeignKey('PageCategory', related_name = 'page_categories', blank = False, null = False)
    
class PageCategory(BaseCategory):
    
    class Meta(BaseCategory.Meta):
        verbose_name_plural = 'Page Categories'
    
class Product(BaseProduct):
    category = models.ManyToManyField('ProductCategory', related_name = 'product_categories', blank = False, null = False)
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d')
    store_link = models.CharField(max_length = 255, blank = True, null = True, default = None)

class ProductCategory(BaseCategory):
    
    class Meta(BaseCategory.Meta):
        verbose_name_plural = 'Product Categories'

class Recipe(BaseRecipe):
    pass
    
class Page(BasePage):
    pass