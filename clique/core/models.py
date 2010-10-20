from django.db import models

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
