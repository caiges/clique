from django.db import models
from django.contrib.auth.models import User
from core.models import Category, SubCategory

class BasePage(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    body = models.TextField(blank = True, null = True, default = None)
    revision = models.IntegerField(blank = False, null = False)
    created_by = models.ForeignKey('User', related_name = "%(class)s_set")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Page(BasePage):
    category = models.ForeignKey(Category, related_name = 'page_categories', blank = False, null = False)
