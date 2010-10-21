from django.db import models

class BaseContentAssociation(models.Model):
    source_model = models.CharField(max_length = 255, blank = False, null = False)
    source_model_id = models.IntegerField(blank = False, null = False)
    target_model = models.CharField(max_length = 255, blank = False, null = False)
    target_model_id = models.IntegerField(blank = False, null = False)
    target_model_count = models.IntegerField(blank = False, null = False, default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
