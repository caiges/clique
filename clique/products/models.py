from django.db import models
from django.contrib.auth.models import User
from core.models import Category

class BaseProduct(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    description = models.CharField(max_length = 200, blank = True, null = True, default = None)
    long_description = models.TextField(blank = True, null = True, default = None)
    product_details = models.TextField(blank = True, null = True, default = None) 
    is_active = models.BooleanField(default = True)
    created_by = models.ForeignKey(User, related_name = "%(class)s_set")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   
    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.name

class Product(BaseProduct):
    category = models.ForeignKey(Category, related_name = 'product_categories', blank = False, null = False)
    product_image = models.ImageField(upload_to = 'product_images/%Y/%m/%d')
    store_link = models.CharField(max_length = 255, blank = True, null = True, default = None)
