from django.db import models
from django.contrib.auth.models import User

class BasePage(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False)
    body = models.TextField(blank = True, null = True, default = None)
    revision = models.IntegerField(blank = False, null = False)
    created_by = models.ForeignKey(User, related_name = "%(class)s_set")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
