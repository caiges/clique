from django.db import models

class BaseContentAssociation(models.Model):
    source_model = models.CharField(max_length = 255, blank = True, null = True, default = None)
    source_model_id = models.IntegerField(blank = True, null = True, default = None)
    target_model = models.CharField(max_length = 255, blank = True, null = True, default = None)
    target_model_id = models.IntegerField(blank = True, null = True, default = None)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
