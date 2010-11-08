from django.db import models

class BaseTag(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        
    def __unicode__(self):
        return u'%s' % self.name
