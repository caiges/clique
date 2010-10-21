from django.db import models

class BaseCategory(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        abstract = True
        
    def __unicode__(self):
        return "%s" % self.name