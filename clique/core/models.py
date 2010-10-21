from django.db import models
from external_apps.pages.models import BasePage
from external_apps.products.models import BaseProduct

class ContentAssocation(models.Model):
    model_name = models.CharField(max_length = 100, blank = False, null = False)
    model_id = models.IntegerField(blank = False, null = False)
    target_model_name = models.CharField(max_length = 100, blank = False, null = False)
    target_model_id = models.IntegerField(blank = False, null = False)

class Category(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name_plural = 'Categories'

class Page(BasePage):
    category = models.ForeignKey(Category, related_name = 'page_categories', blank = False, null = False)
    
class Product(BaseProduct):
    category = models.ManyToManyField(Category, related_name = 'product_categories', blank = False, null = False)
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d')
    store_link = models.CharField(max_length = 255, blank = True, null = True, default = None)