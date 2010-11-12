from django.db import models
from django.contrib.auth.models import User

class BasePage(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    page_title = models.CharField(max_length = 100, blank = True, null = True, default = None, help_text = "Page Title")
    url = models.CharField(max_length = 1000, blank = True, default = None, help_text = "URL will be appended to /...")
    meta_description = models.CharField(max_length = 500, blank = True, null = True)
    meta_keywords = models.CharField(max_length = 500, blank = True, null = True, default = None, help_text = 'Format: (keyword-one, keyword-two)')
    body = models.TextField(blank = True, null = True, default = None)
    make_live = models.BooleanField(default = True)
    user = models.ForeignKey(User, related_name = "%(class)s_set")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        
    def __unicode__(self):
        return u'%s' % self.name
