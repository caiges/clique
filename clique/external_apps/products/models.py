from django.db import models
from django.contrib.auth.models import User

class BaseProduct(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    url = models.CharField(max_length = 1000, blank = False, null = False, help_text = "URL will be appended to /products/...")
    meta_description = models.CharField(max_length = 500, blank = True, null = True)
    meta_keywords = models.CharField(max_length = 500, blank = True, null = True, default = None, help_text = 'Format: (keyword-one, keyword-two)')
    description = models.CharField(max_length = 200, blank = True, null = True, default = None)
    long_description = models.TextField(blank = True, null = True, default = None)
    product_details = models.TextField(blank = True, null = True, default = None) 
    is_active = models.BooleanField(default = True)
    user = models.ForeignKey(User, related_name = "%(class)s_set")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   
    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.name
