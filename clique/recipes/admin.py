from django.contrib import admin
from models import *

class RecipeAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Recipe, RecipeAdmin)